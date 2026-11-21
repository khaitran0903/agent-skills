#!/usr/bin/env python3
"""Check evidence consistency against externally supplied acceptance and run context.

Standard library only. Does not execute report commands or authorize release.
"""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys

VERDICTS = {'Passed', 'Failed', 'Not Run', 'Not Applicable'}
LIMITATION = 'Checks evidence consistency; does not prove claims or authorize acceptance/release.'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def text(value, label):
    require(isinstance(value, str) and bool(value.strip()), f'{label}: expected nonempty string')


def integer(value, label):
    require(type(value) is int and value >= 0, f'{label}: expected nonnegative integer')


def strings(value, label):
    require(isinstance(value, list) and bool(value), f'{label}: expected nonempty list')
    for item in value:
        text(item, label)


def document(value, label):
    require(isinstance(value, dict), f'{label}: expected object')
    require(type(value.get('schema_version')) is int and value['schema_version'] == 1,
            f'{label}: unsupported schema_version')


def candidate(value, label):
    require(isinstance(value, dict) and set(value) == {'revision', 'snapshot'},
            f'{label}: expected revision and snapshot')
    for field in ('revision', 'snapshot'):
        text(value[field], f'{label}.{field}')


def identity(value, label):
    document(value, label)
    text(value.get('run_id'), f'{label}.run_id')
    text(value.get('environment'), f'{label}.environment')
    candidate(value.get('candidate'), f'{label}.candidate')


def indexed(value, label):
    require(isinstance(value, list), f'{label}: expected list')
    result = {}
    for item in value:
        require(isinstance(item, dict), f'{label}: expected check object')
        text(item.get('id'), f'{label}.id')
        require(item['id'] not in result, f'{label}: duplicate check {item["id"]}')
        result[item['id']] = item
    return result


def artifacts(value, label):
    require(isinstance(value, list), f'{label}: expected artifact list')
    paths = set()
    for item in value:
        require(isinstance(item, dict), f'{label}: expected artifact object')
        path = item.get('path')
        text(path, f'{label}.path')
        require('\\' not in path and ':' not in path and not path.startswith('/')
                and all(part not in ('', '.', '..') for part in path.split('/')),
                f'{label}: unsafe artifact path {path}')
        require(path not in paths, f'{label}: duplicate artifact path {path}')
        paths.add(path)
        require(isinstance(item.get('sha256'), str)
                and re.fullmatch(r'[0-9a-f]{64}', item['sha256']), f'{label}: invalid sha256')


def execution(value, label, observed=False):
    require(isinstance(value, dict), f'{label}: expected execution object')
    strings(value.get('command'), f'{label}.command')
    text(value.get('cwd'), f'{label}.cwd')
    exit_code = value.get('exit_code')
    require(type(exit_code) is int or (observed and exit_code is None),
            f'{label}.exit_code: expected integer')
    if observed:
        require(value.get('outcome') in ('completed', 'timeout', 'error'), f'{label}: invalid outcome')
        require(value['outcome'] != 'completed' or type(exit_code) is int,
                f'{label}: completed command needs exit_code')
    if 'tests' in value:
        counts = value['tests']
        require(isinstance(counts, dict), f'{label}.tests: expected object')
        for field in ('total', 'passed', 'failed', 'skipped'):
            integer(counts.get(field), f'{label}.tests.{field}')
        require(counts['total'] == counts['passed'] + counts['failed'] + counts['skipped'],
                f'{label}.tests: inconsistent inventory')


def read_json(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, f'{path}: duplicate JSON key {key}')
            result[key] = value
        return result
    return json.loads(Path(path).read_text(encoding='utf-8'), object_pairs_hook=unique)


def artifact_problems(items, root, label):
    problems = []
    for item in items:
        current = root
        for part in PurePosixPath(item['path']).parts:
            current = current / part
            if current.is_symlink() or getattr(current, 'is_junction', lambda: False)():
                problems.append(f'{label}: artifact link/junction is unsupported: {item["path"]}')
                break
        else:
            if not current.resolve().is_relative_to(root) or not current.is_file():
                problems.append(f'{label}: missing artifact {item["path"]}')
            elif hashlib.sha256(current.read_bytes()).hexdigest() != item['sha256']:
                problems.append(f'{label}: artifact hash mismatch: {item["path"]}')
    return problems


def evaluate(contract, context, report, artifact_root, observations=None):
    """Raise for malformed input; return unmet acceptance for well-formed reports."""
    document(contract, 'contract')
    text(contract.get('contract_id'), 'contract.contract_id')
    required = indexed(contract.get('checks'), 'contract.checks')
    require(bool(required), 'contract.checks: acceptance must not be empty')
    for check_id, check in required.items():
        text(check.get('expected'), f'{check_id}.expected')
        strings(check.get('kinds'), f'{check_id}.kinds')
        require(check.get('execution') in ('command', 'manual'), f'{check_id}: invalid execution mode')
        if 'minimum_tests' in check:
            integer(check['minimum_tests'], f'{check_id}.minimum_tests')
            require(check['execution'] == 'command', f'{check_id}: minimum_tests requires command mode')
    identity(context, 'context')
    identity(report, 'report')
    text(report.get('contract_id'), 'report.contract_id')
    require(isinstance(report.get('limitations'), list)
            and all(isinstance(item, str) and item.strip() for item in report['limitations']),
            'report.limitations: expected list of nonempty strings (may be empty)')
    results = indexed(report.get('checks'), 'report.checks')
    for check_id, check in results.items():
        text(check.get('kind'), f'{check_id}.kind')
        require(check.get('verdict') in VERDICTS, f'{check_id}: invalid verdict')
        text(check.get('expected'), f'{check_id}.expected')
        text(check.get('actual'), f'{check_id}.actual')
        artifacts(check.get('artifacts'), f'{check_id}.artifacts')
        if check['verdict'] in ('Not Run', 'Not Applicable'):
            text(check.get('reason'), f'{check_id}.reason')
        if 'execution' in check:
            execution(check['execution'], check_id)
        if 'steps' in check:
            strings(check['steps'], f'{check_id}.steps')
    observed = {}
    if observations is not None:
        identity(observations, 'observations')
        observed = indexed(observations.get('checks'), 'observations.checks')
        for check_id, check in observed.items():
            text(check.get('kind'), f'observations.{check_id}.kind')
            execution(check.get('execution'), f'observations.{check_id}', observed=True)
            artifacts(check.get('artifacts'), f'observations.{check_id}.artifacts')
    root = Path(artifact_root).resolve(strict=True)
    require(root.is_dir(), 'artifact_root: expected directory')
    unmet = []
    if report['contract_id'] != contract['contract_id']:
        unmet.append('report: contract_id differs from external acceptance')
    for label, value in [('report', report), *([('observations', observations)] if observations is not None else [])]:
        for field in ('run_id', 'candidate', 'environment'):
            if value[field] != context[field]:
                unmet.append(f'{label}: {field} differs from external context')
    for check_id in sorted(set(results) - set(required)):
        unmet.append(f'{check_id}: check is outside external acceptance')
    for check_id, rule in required.items():
        if check_id not in results:
            unmet.append(f'{check_id}: missing required check')
            continue
        check = results[check_id]
        if check['expected'] != rule['expected']:
            unmet.append(f'{check_id}: expected differs from external acceptance')
        unmet.extend(artifact_problems(check['artifacts'], root, check_id))
        if check['verdict'] != 'Passed':
            unmet.append(f'{check_id}: required check is {check["verdict"]}')
            continue
        if check['kind'] not in rule['kinds']:
            unmet.append(f'{check_id}: evidence kind {check["kind"]} does not satisfy acceptance')
        if not check['artifacts']:
            unmet.append(f'{check_id}: Passed needs evidence artifacts')
        if rule['execution'] == 'manual':
            if not check.get('steps'):
                unmet.append(f'{check_id}: manual check needs observed steps')
            continue
        if 'execution' not in check:
            unmet.append(f'{check_id}: command check needs execution')
            continue
        claimed = check['execution']
        if check_id not in observed:
            unmet.append(f'{check_id}: missing independent runner observation')
            continue
        actual = observed[check_id]
        run = actual['execution']
        if actual['kind'] != check['kind']:
            unmet.append(f'{check_id}: evidence kind differs from runner observation')
        if (claimed != {key: value for key, value in run.items() if key != 'outcome'}):
            unmet.append(f'{check_id}: claimed execution differs from runner observation')
        if sorted(check['artifacts'], key=lambda item: item['path']) != sorted(actual['artifacts'], key=lambda item: item['path']):
            unmet.append(f'{check_id}: claimed artifacts differ from runner observation')
        unmet.extend(artifact_problems(actual['artifacts'], root, f'runner.{check_id}'))
        if run['outcome'] != 'completed' or run['exit_code'] != 0:
            unmet.append(f'{check_id}: runner did not complete successfully')
        counts = run.get('tests')
        if counts and counts['failed']:
            unmet.append(f'{check_id}: runner recorded failed tests')
        if 'minimum_tests' in rule:
            if counts is None or counts['passed'] < rule['minimum_tests']:
                unmet.append(f'{check_id}: insufficient executed passing tests')
    return {'report_valid': True, 'acceptance_met': not unmet, 'unmet': unmet, 'limitation': LIMITATION}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--contract', required=True, help='Acceptance maintained outside the report')
    parser.add_argument('--context', required=True, help='Expected run/candidate/environment from caller')
    parser.add_argument('--report', required=True)
    parser.add_argument('--artifacts', required=True, help='Root of local run artifacts')
    parser.add_argument('--observations', help='Facts captured by the trusted runner, not report author')
    args = parser.parse_args()
    try:
        result = evaluate(read_json(args.contract), read_json(args.context), read_json(args.report),
                          args.artifacts, read_json(args.observations) if args.observations else None)
    except (ValueError, OSError, TypeError) as error:
        print(json.dumps({'report_valid': False, 'acceptance_met': False,
                          'errors': [str(error)], 'limitation': LIMITATION}, ensure_ascii=False))
        return 2
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result['acceptance_met'] else 1


if __name__ == '__main__':
    sys.exit(main())
