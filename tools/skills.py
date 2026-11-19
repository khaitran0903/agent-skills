#!/usr/bin/env python3
"""Validate and distribute reviewed skills. Standard library only; sync defaults to preview."""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = 'https://github.com/khaitran0903/agent-skills.git'
NAME = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*\Z')
VERSION = re.compile(r'\d+\.\d+\.\d+\Z')
HASH = re.compile(r'[0-9a-f]{64}\Z')


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def safe_path(root, relative):
    """Reject traversal, drive paths and links/junctions before any filesystem mutation."""
    parts = PurePosixPath(relative).parts
    if not parts or PurePosixPath(relative).is_absolute() or any(p in ('.', '..') for p in parts) or ':' in relative or '\\' in relative:
        raise ValueError(f'Unsafe path: {relative}')
    current = root
    for part in parts:
        current = current / part
        if current.is_symlink() or getattr(current, 'is_junction', lambda: False)():
            raise ValueError(f'Link/junction is not supported: {current}')
    if not current.resolve().is_relative_to(root.resolve()):
        raise ValueError(f'Path escapes root: {relative}')
    return current


def bundle(directory):
    if not directory.exists():
        return {}
    if not directory.is_dir():
        raise ValueError(f'Expected directory: {directory}')
    result = {}
    for folder, dirs, files in os.walk(directory, followlinks=False):
        for name in dirs + files:
            item = Path(folder) / name
            relative = item.relative_to(directory).as_posix()
            safe_path(directory, relative)
            if name in files:
                if not item.is_file():
                    raise ValueError(f'Expected regular file: {item}')
                result[relative] = item.read_bytes()
    return result


def hashes(files):
    return {p: hashlib.sha256(data).hexdigest() for p, data in sorted(files.items())}


def catalog():
    data = read_json(ROOT / 'catalog.json')
    if data.get('schema_version') != 1 or data.get('repository') != REPOSITORY:
        raise ValueError('Unsupported catalog schema/repository')
    result = {}
    for item in data['skills']:
        name = item['name']
        if not NAME.fullmatch(name) or len(name) > 64 or name in result or not VERSION.fullmatch(item['version']):
            raise ValueError(f'Invalid/duplicate catalog entry: {name}')
        if item['path'] != f'skills/{name}':
            raise ValueError(f'Unexpected package path: {name}')
        safe_path(ROOT, item['path'])
        result[name] = item
    return result


def validate():
    items = catalog()
    actual = {p.name for p in (ROOT / 'skills').iterdir() if p.is_dir()}
    if actual != set(items):
        raise ValueError('Catalog and skills directories differ')
    for name, item in items.items():
        directory = safe_path(ROOT, item['path'])
        files = bundle(directory)
        entry = files['SKILL.md'].decode('utf-8')
        match = re.match(r'\A---\nname: ([^\n]+)\ndescription: ([^\n]+)\n---\n', entry)
        if not match or match[1] != name or not match[2].strip() or len(match[2]) > 1024:
            raise ValueError(f'Invalid frontmatter: {name}')
        if '[TODO:' in entry:
            raise ValueError(f'Unfinished scaffold: {name}')
        for source in item['source_skills']:
            if not safe_path(ROOT, source).is_file():
                raise ValueError(f'Missing source: {source}')
        # Each installable package must work without siblings or repository docs.
        check_links(directory, [directory / p for p in files if p.endswith('.md')], directory)
    manifest = read_json(ROOT / 'sources/manifest.json')
    if manifest.get('schema_version') != 1:
        raise ValueError('Unsupported source manifest')
    recorded = set()
    for source in manifest['sources']:
        kind = source.get('kind', 'git')
        if kind == 'git':
            if not isinstance(source.get('commit'), str) or not re.fullmatch(r'[0-9a-f]{40}', source['commit']):
                raise ValueError('Invalid source commit')
        elif kind == 'workspace':
            if source.get('commit') is not None or source.get('repository') is not None:
                raise ValueError('Workspace source must not claim a Git commit/repository')
            if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', source.get('captured_on', '')) or not source.get('origin'):
                raise ValueError('Workspace source requires capture date and origin')
        else:
            raise ValueError(f'Unsupported source kind: {kind}')
        for item in source['files']:
            relative = item['snapshot_path']
            if relative in recorded or relative != f'sources/{source["id"]}/{item["source_path"]}':
                raise ValueError(f'Invalid/duplicate snapshot: {relative}')
            recorded.add(relative)
            if hashlib.sha256(safe_path(ROOT, relative).read_bytes()).hexdigest() != item['sha256']:
                raise ValueError(f'Snapshot hash mismatch: {relative}')
    actual_sources = {f'sources/{source["id"]}/{p}' for source in manifest['sources'] for p in bundle(ROOT / 'sources' / source['id'])}
    if actual_sources != recorded:
        raise ValueError('Snapshot file inventory differs from manifest')
    docs = [*ROOT.glob('*.md'), *(ROOT / 'docs').glob('*.md'), *(ROOT / 'profiles').glob('*.md'), ROOT / 'sources/README.md']
    check_links(ROOT, docs, ROOT)
    print(f'Validated {len(items)} portable skills and {len(recorded)} source files; local links and hashes OK.')


def check_links(root, documents, boundary):
    for document in documents:
        for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', document.read_text(encoding='utf-8')):
            if target.startswith(('https://', 'http://', '#', 'mailto:')):
                continue
            target = target.split('#', 1)[0]
            resolved = (document.parent / target).resolve()
            if not resolved.is_relative_to(boundary.resolve()) or not resolved.exists():
                raise ValueError(f'Missing/nonportable link in {document.relative_to(root)}: {target}')


def upstream_commit():
    git = lambda *args: subprocess.check_output(['git', '-C', str(ROOT), *args], text=True, encoding='utf-8').strip()
    commit = git('rev-parse', 'HEAD')
    if git('status', '--porcelain', '--untracked-files=all', '--', 'skills', 'catalog.json', 'tools/skills.py'):
        raise ValueError('Source packages/catalog/tool have uncommitted changes; commit before sync')
    return commit


def read_lock(path):
    if not path.exists():
        return {'schema_version': 1, 'repository': REPOSITORY, 'skills': {}}
    lock = read_json(path)
    if lock.get('schema_version') != 1 or lock.get('repository') != REPOSITORY or not isinstance(lock.get('skills'), dict):
        raise ValueError('Unsupported lock schema/repository; keep the existing lock for review')
    for name, entry in lock['skills'].items():
        if not NAME.fullmatch(name) or not VERSION.fullmatch(entry['version']) or not re.fullmatch(r'[0-9a-f]{40}', entry['upstream_commit']):
            raise ValueError(f'Invalid locked skill: {name}')
        if not isinstance(entry.get('files'), dict) or 'SKILL.md' not in entry['files']:
            raise ValueError(f'Invalid locked file inventory: {name}')
        for relative, digest in entry['files'].items():
            safe_path(path.parent, relative)
            if not isinstance(digest, str) or not HASH.fullmatch(digest):
                raise ValueError(f'Invalid locked hash: {name}/{relative}')
    return lock


def sync(args):
    items = catalog()
    project = Path(args.project).resolve(strict=True)
    if not project.is_dir() or project == ROOT or project.is_relative_to(ROOT) or ROOT.is_relative_to(project):
        raise ValueError('Choose an existing project directory outside the source checkout')
    commit = upstream_commit()
    lock_path = safe_path(project, '.agents/agent-skills.lock.json')
    temporary = safe_path(project, '.agents/agent-skills.lock.json.tmp')
    if temporary.exists():
        raise ValueError('Temporary lock exists; review interrupted sync before retrying')
    lock = read_lock(lock_path)
    names = sorted(set(args.skill or lock['skills']))
    if not names:
        raise ValueError('First install requires one or more --skill names')
    plans = []
    conflicts = []
    for name in names:
        if name not in items:
            raise ValueError(f'Unknown/unavailable skill: {name}')
        destination = safe_path(project, f'.agents/skills/{name}')
        current = hashes(bundle(destination))
        old = lock['skills'].get(name)
        if old is None and destination.exists():
            conflicts.append(f'{name}: destination exists without ownership in lock')
        elif old is not None and current != old['files']:
            changed = sorted(p for p in set(current) | set(old['files']) if current.get(p) != old['files'].get(p))
            conflicts.append(f'{name}: local edits/additions/deletions: {", ".join(changed)}')
        files = bundle(safe_path(ROOT, items[name]['path']))
        if 'SKILL.md' not in files:
            raise ValueError(f'Missing package entrypoint: {name}')
        incoming = hashes(files)
        added = sorted(set(incoming) - set(current))
        removed = sorted(set(current) - set(incoming))
        modified = sorted(p for p in set(current) & set(incoming) if current[p] != incoming[p])
        print(f'{name} -> {items[name]["version"]}: +{len(added)} ~{len(modified)} -{len(removed)}')
        for label, paths in [('ADD', added), ('MODIFY', modified), ('REMOVE', removed)]:
            for path in paths:
                print(f'  {label} {path}')
        plans.append((name, destination, files, removed, incoming))
    if conflicts:
        raise ValueError('No files written. Conflicts:\n' + '\n'.join(conflicts))
    if not args.apply:
        print('Preview only. Add --apply to write packages and lock.')
        return
    # All selected packages have been checked before the first write. Run one sync at a time.
    for name, destination, files, removed, incoming in plans:
        for relative in removed:
            safe_path(destination, relative).unlink()
        # Remove empty old directories so upstream can change a directory into a file.
        if destination.exists():
            for folder in sorted(destination.rglob('*'), key=lambda p: len(p.parts), reverse=True):
                if folder.is_dir() and not any(folder.iterdir()):
                    folder.rmdir()
        for relative, data in files.items():
            target = safe_path(destination, relative)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        lock['skills'][name] = {'version': items[name]['version'], 'upstream_commit': commit, 'files': incoming}
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with temporary.open('x', encoding='utf-8', newline='\n') as handle:
        handle.write(json.dumps(lock, ensure_ascii=False, indent=2) + '\n')
    temporary.replace(lock_path)
    print(f'Applied {len(plans)} skill(s) from {commit}. Review project diff and run relevant checks.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('list')
    sub.add_parser('validate')
    install = sub.add_parser('sync')
    install.add_argument('--project', required=True)
    install.add_argument('--skill', action='append', help='Repeat to select packages; omitted selects installed skills')
    install.add_argument('--apply', action='store_true', help='Write changes; default is preview')
    args = parser.parse_args()
    try:
        if args.command == 'list':
            for name, item in catalog().items():
                print(f'{name:30} {item["version"]:8} {item["category"]}')
        elif args.command == 'validate':
            validate()
        else:
            sync(args)
    except (ValueError, KeyError, TypeError, OSError, subprocess.CalledProcessError) as error:
        print(f'ERROR: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
