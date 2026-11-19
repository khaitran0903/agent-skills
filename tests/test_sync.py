"""Exercise real filesystem/Git boundaries without touching ITS or PBC."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]


class SyncTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='agent-skills-test-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / 'source'
        self.project = self.root / 'project'
        self.project.mkdir()
        self.source.mkdir()
        for name in ['skills', 'tools']:
            shutil.copytree(REPO / name, self.source / name, ignore=shutil.ignore_patterns('__pycache__'))
        shutil.copy2(REPO / 'catalog.json', self.source / 'catalog.json')
        self.git('init', '-q')
        self.git('config', 'user.name', 'Skill Sync Test')
        self.git('config', 'user.email', 'tests@example.invalid')
        self.git('config', 'core.autocrlf', 'false')
        self.commit()
        self.lock = self.project / '.agents/agent-skills.lock.json'
        self.installed = self.project / '.agents/skills/delivery-planning'

    def git(self, *args):
        return subprocess.check_output(['git', '-C', str(self.source), *args], stderr=subprocess.STDOUT, text=True).strip()

    def commit(self):
        self.git('add', '.')
        self.git('commit', '-qm', 'Test source candidate')
        return self.git('rev-parse', 'HEAD')

    def run_sync(self, *args, ok=True):
        result = subprocess.run([sys.executable, str(self.source / 'tools/skills.py'), 'sync', '--project', str(self.project), *args], capture_output=True, text=True, encoding='utf-8')
        self.assertEqual(result.returncode, 0 if ok else 1, result.stdout + result.stderr)
        return result

    def install(self, *names):
        args = [value for name in (names or ('delivery-planning',)) for value in ('--skill', name)]
        self.run_sync(*args, '--apply')

    def snapshot(self):
        return {p.relative_to(self.project).as_posix(): p.read_bytes() for p in self.project.rglob('*') if p.is_file()}

    def test_preview_has_no_side_effect_and_first_install_requires_selection(self):
        self.run_sync(ok=False)
        self.run_sync('--skill', 'delivery-planning')
        self.assertEqual(self.snapshot(), {})
        self.assertFalse((self.project / '.agents').exists())

    def test_install_records_exact_bytes_commit_and_is_repeatable(self):
        self.install()
        lock = json.loads(self.lock.read_text())
        entry = lock['skills']['delivery-planning']
        self.assertEqual(entry['upstream_commit'], self.git('rev-parse', 'HEAD'))
        for relative, digest in entry['files'].items():
            data = (self.installed / relative).read_bytes()
            self.assertEqual(data, (self.source / 'skills/delivery-planning' / relative).read_bytes())
            self.assertEqual(hashlib.sha256(data).hexdigest(), digest)
        before = self.snapshot()
        self.run_sync('--apply')
        self.assertEqual(self.snapshot(), before)

    def test_update_and_rollback_follow_selected_commit(self):
        self.install()
        before = self.snapshot()
        old_commit = self.git('rev-parse', 'HEAD')
        entry = self.source / 'skills/delivery-planning/SKILL.md'
        entry.write_bytes(entry.read_bytes() + b'\nAdditional reviewed guidance.\n')
        new_commit = self.commit()
        self.run_sync()
        self.assertEqual(self.snapshot(), before)
        self.run_sync('--apply')
        self.assertEqual(json.loads(self.lock.read_text())['skills']['delivery-planning']['upstream_commit'], new_commit)
        self.git('checkout', '--detach', old_commit)
        self.run_sync('--apply')
        self.assertEqual(self.snapshot(), before)

    def test_all_selected_packages_are_preserved_when_one_is_modified(self):
        self.install('delivery-planning', 'ui-design-system')
        (self.installed / 'SKILL.md').write_bytes(b'local customization\n')
        source_ui = self.source / 'skills/ui-design-system/SKILL.md'
        source_ui.write_bytes(source_ui.read_bytes() + b'\nUpstream change\n')
        self.commit()
        before = self.snapshot()
        result = self.run_sync('--apply', ok=False)
        self.assertIn('local edits', result.stderr)
        self.assertEqual(self.snapshot(), before)

    def test_added_local_file_is_preserved(self):
        self.install()
        (self.installed / 'local.md').write_text('local decision')
        before = self.snapshot()
        self.run_sync('--apply', ok=False)
        self.assertEqual(self.snapshot(), before)

    def test_deleted_local_file_is_not_silently_restored(self):
        self.install()
        (self.installed / 'SKILL.md').unlink()
        before = self.snapshot()
        self.run_sync('--apply', ok=False)
        self.assertEqual(self.snapshot(), before)

    def test_existing_unmanaged_directory_is_not_adopted(self):
        self.installed.mkdir(parents=True)
        (self.installed / 'SKILL.md').write_text('existing project skill')
        before = self.snapshot()
        self.run_sync('--skill', 'delivery-planning', '--apply', ok=False)
        self.assertEqual(self.snapshot(), before)

    def test_upstream_removed_file_and_directory_to_file_transition(self):
        self.install()
        old = self.source / 'skills/delivery-planning/agents/openai.yaml'
        old.unlink()
        old.parent.rmdir()
        old.parent.write_bytes(b'new upstream flat file\n')
        self.commit()
        self.run_sync('--apply')
        self.assertTrue((self.installed / 'agents').is_file())
        self.assertEqual((self.installed / 'agents').read_bytes(), b'new upstream flat file\n')

    def test_partial_update_keeps_other_skill_provenance(self):
        self.install('delivery-planning', 'ui-design-system')
        old_ui = json.loads(self.lock.read_text())['skills']['ui-design-system']
        entry = self.source / 'skills/delivery-planning/SKILL.md'
        entry.write_bytes(entry.read_bytes() + b'\nNew upstream revision\n')
        self.commit()
        self.run_sync('--skill', 'delivery-planning', '--apply')
        self.assertEqual(json.loads(self.lock.read_text())['skills']['ui-design-system'], old_ui)

    def test_dirty_source_is_rejected_before_project_write(self):
        entry = self.source / 'skills/delivery-planning/SKILL.md'
        entry.write_bytes(entry.read_bytes() + b'\nUncommitted\n')
        self.run_sync('--skill', 'delivery-planning', '--apply', ok=False)
        self.assertEqual(self.snapshot(), {})

    def test_malicious_lock_path_cannot_delete_outside_package(self):
        self.install()
        lock = json.loads(self.lock.read_text())
        lock['skills']['delivery-planning']['files']['../../../outside.txt'] = '0' * 64
        self.lock.write_text(json.dumps(lock))
        outside = self.root / 'outside.txt'
        outside.write_text('keep')
        before = self.snapshot()
        self.run_sync('--apply', ok=False)
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(outside.read_text(), 'keep')

    def test_catalog_path_escape_is_rejected(self):
        path = self.source / 'catalog.json'
        data = json.loads(path.read_text())
        data['skills'][0]['path'] = '../outside'
        path.write_text(json.dumps(data))
        self.commit()
        self.run_sync('--skill', 'delivery-planning', '--apply', ok=False)
        self.assertEqual(self.snapshot(), {})

    def test_interrupted_lock_marker_blocks_before_any_write(self):
        self.install()
        self.lock.with_suffix('.json.tmp').write_text('interrupted')
        before = self.snapshot()
        self.run_sync('--apply', ok=False)
        self.assertEqual(self.snapshot(), before)

    def test_linked_destination_does_not_modify_outside_directory(self):
        outside = self.root / 'outside'
        outside.mkdir()
        (outside / 'keep.txt').write_text('keep')
        self.installed.parent.mkdir(parents=True)
        try:
            self.installed.symlink_to(outside, target_is_directory=True)
        except OSError:
            if os.name != 'nt':
                self.skipTest('Creating symlinks is unavailable on this host')
            result = subprocess.run(['cmd.exe', '/c', 'mklink', '/J', str(self.installed), str(outside)], capture_output=True)
            if result.returncode:
                self.skipTest('Creating links/junctions is unavailable on this host')
        self.run_sync('--skill', 'delivery-planning', '--apply', ok=False)
        self.assertEqual({p.name: p.read_text() for p in outside.iterdir()}, {'keep.txt': 'keep'})


if __name__ == '__main__':
    unittest.main()
