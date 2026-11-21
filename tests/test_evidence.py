"""Exercise the installed QC helper with real subprocess outcomes and corrupted evidence."""
import copy
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

PACKAGE = Path(__file__).resolve().parents[1] / 'skills/qc-independent-verification'


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='qc-evidence-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        installed = self.root / 'installed-qc'
        shutil.copytree(PACKAGE, installed)
        self.script = installed / 'scripts/check_evidence.py'
        self.contract = {'schema_version': 1, 'contract_id': 'acceptance-v1', 'checks': [
            {'id': 'AC-1', 'expected': 'Both independent assertions hold.',
             'kinds': ['unit'], 'execution': 'command', 'minimum_tests': 2}]}
        self.context = {'schema_version': 1, 'run_id': 'run-current', 'environment': 'isolated Python',
                        'candidate': {'revision': 'a' * 40, 'snapshot': 'sha256:' + 'b' * 64}}
        self.report = dict(copy.deepcopy(self.context), contract_id='acceptance-v1',
                           limitations=['Synthetic runner, no application integration.'], checks=[])
        self.observations = dict(copy.deepcopy(self.context), checks=[])
        self.record_run()

    def record_run(self, wrong=False, swallow=False):
        code = '''import json, sys
failed = 0
for actual, expected in [(100, int(sys.argv[1])), (200, 200)]:
    try:
        assert actual == expected, f'expected={expected}, actual={actual}'
        print('assertion passed')
    except AssertionError as error:
        failed += 1
        print(f'assertion failed: {error}')
print(json.dumps({'total': 2, 'passed': 2 - failed, 'failed': failed, 'skipped': 0}))
sys.exit(0 if sys.argv[2] == 'swallow' or failed == 0 else 3)
'''
        command = [sys.executable, '-c', code, '101' if wrong else '100', 'swallow' if swallow else 'propagate']
        completed = subprocess.run(command, cwd=self.root, capture_output=True, text=True, check=False)
        self.assertEqual(completed.returncode, 0 if swallow or not wrong else 3)
        log = completed.stdout.encode('utf-8')
        (self.root / 'runner.log').write_bytes(log)
        evidence = [{'path': 'runner.log', 'sha256': hashlib.sha256(log).hexdigest()}]
        execution = {'command': command, 'cwd': str(self.root), 'exit_code': completed.returncode,
                     'tests': json.loads(completed.stdout.splitlines()[-1])}
        self.report['checks'] = [{'id': 'AC-1', 'kind': 'unit',
                                 'verdict': 'Failed' if wrong else 'Passed',
                                 'expected': 'Both independent assertions hold.',
                                 'actual': completed.stdout.strip(), 'execution': copy.deepcopy(execution),
                                 'artifacts': copy.deepcopy(evidence)}]
        self.observations['checks'] = [{'id': 'AC-1', 'kind': 'unit',
                                       'execution': dict(execution, outcome='completed'),
                                       'artifacts': evidence}]

    def invoke(self, observations=True):
        for name, value in [('contract', self.contract), ('context', self.context),
                            ('report', self.report), ('observations', self.observations)]:
            (self.root / f'{name}.json').write_text(json.dumps(value), encoding='utf-8')
        command = [sys.executable, str(self.script), '--contract', str(self.root / 'contract.json'),
                   '--context', str(self.root / 'context.json'), '--report', str(self.root / 'report.json'),
                   '--artifacts', str(self.root)]
        if observations:
            command += ['--observations', str(self.root / 'observations.json')]
        completed = subprocess.run(command, cwd=self.root, capture_output=True, text=True, check=False)
        self.assertEqual(completed.stderr, '')
        return completed.returncode, json.loads(completed.stdout)

    def assert_blocked(self, fragment):
        code, result = self.invoke()
        self.assertEqual(code, 1, result)
        self.assertTrue(result['report_valid'])
        self.assertFalse(result['acceptance_met'])
        self.assertTrue(any(fragment in item for item in result['unmet']), result)

    def test_installed_package_accepts_current_successful_run(self):
        code, result = self.invoke()
        self.assertEqual(code, 0, result)
        self.assertTrue(result['report_valid'])
        self.assertTrue(result['acceptance_met'])

    def test_missing_acceptance_cannot_be_hidden_by_report_inventory(self):
        self.contract['checks'].append({'id': 'AC-2', 'expected': 'The manual requirement holds.',
                                        'kinds': ['manual'], 'execution': 'manual'})
        self.assert_blocked('AC-2: missing required check')

    def test_truthful_failure_is_valid_report_but_does_not_meet_acceptance(self):
        self.record_run(wrong=True)
        self.assert_blocked('required check is Failed')

    def test_claimed_pass_cannot_override_actual_process_failure(self):
        self.record_run(wrong=True)
        check = self.report['checks'][0]
        check['verdict'] = 'Passed'
        check['execution']['exit_code'] = 0
        check['execution']['tests'] = {'total': 2, 'passed': 2, 'failed': 0, 'skipped': 0}
        self.assert_blocked('runner did not complete successfully')

    def test_report_cannot_replace_expected_to_match_actual(self):
        self.report['checks'][0]['expected'] = 'Whatever actual returns is acceptable.'
        self.assert_blocked('expected differs from external acceptance')

    def test_last_passing_assertion_and_swallowed_exit_do_not_hide_failure(self):
        self.record_run(wrong=True, swallow=True)
        self.report['checks'][0]['verdict'] = 'Passed'
        self.assert_blocked('runner recorded failed tests')

    def test_fault_removed_same_runner_can_pass_again(self):
        self.record_run(wrong=True)
        self.assert_blocked('required check is Failed')
        self.record_run()
        code, result = self.invoke()
        self.assertEqual(code, 0, result)

    def test_zero_tests_and_all_skipped_do_not_meet_required_execution(self):
        for counts in ({'total': 0, 'passed': 0, 'failed': 0, 'skipped': 0},
                       {'total': 2, 'passed': 0, 'failed': 0, 'skipped': 2}):
            with self.subTest(counts=counts):
                self.report['checks'][0]['execution']['tests'] = counts
                self.observations['checks'][0]['execution']['tests'] = counts
                self.assert_blocked('insufficient executed passing tests')

    def test_build_command_does_not_require_test_counts_without_test_acceptance(self):
        del self.contract['checks'][0]['minimum_tests']
        del self.report['checks'][0]['execution']['tests']
        del self.observations['checks'][0]['execution']['tests']
        code, result = self.invoke()
        self.assertEqual(code, 0, result)

    def test_old_report_cannot_be_presented_as_current_run(self):
        self.context['run_id'] = 'run-new-after-timeout'
        self.assert_blocked('run_id differs from external context')

    def test_timeout_does_not_accept_success_report_left_in_place(self):
        observation = self.observations['checks'][0]['execution']
        observation['outcome'] = 'timeout'
        observation['exit_code'] = None
        self.assert_blocked('runner did not complete successfully')

    def test_candidate_includes_dirty_snapshot_not_just_head_revision(self):
        self.context['candidate']['snapshot'] = 'sha256:' + 'c' * 64
        self.assert_blocked('candidate differs from external context')

    def test_identified_dirty_candidate_is_allowed_without_forcing_commit(self):
        for value in (self.context, self.report, self.observations):
            value['candidate']['snapshot'] = 'sha256:' + 'd' * 64
        code, result = self.invoke()
        self.assertEqual(code, 0, result)

    def test_environment_and_contract_version_are_bound_externally(self):
        self.context['environment'] = 'another environment'
        self.report['contract_id'] = 'different-contract'
        self.assert_blocked('environment differs from external context')
        self.assert_blocked('contract_id differs from external acceptance')

    def test_mock_evidence_does_not_satisfy_browser_acceptance(self):
        self.contract['checks'][0]['kinds'] = ['browser']
        self.report['checks'][0]['kind'] = 'mock'
        self.observations['checks'][0]['kind'] = 'mock'
        self.assert_blocked('evidence kind mock does not satisfy acceptance')

    def test_automated_pass_needs_runner_observation(self):
        code, result = self.invoke(observations=False)
        self.assertEqual(code, 1, result)
        self.assertIn('AC-1: missing independent runner observation', result['unmet'])

    def test_command_and_artifacts_cannot_be_relabelled_in_report(self):
        self.report['checks'][0]['execution']['command'] = ['other-command']
        self.assert_blocked('claimed execution differs from runner observation')

    def test_artifact_deletion_and_tampering_are_detected(self):
        (self.root / 'runner.log').write_text('replaced', encoding='utf-8')
        self.assert_blocked('artifact hash mismatch')
        (self.root / 'runner.log').unlink()
        self.assert_blocked('missing artifact')

    def test_pass_without_artifacts_is_not_accepted(self):
        self.report['checks'][0]['artifacts'] = []
        self.assert_blocked('Passed needs evidence artifacts')

    def test_manual_review_does_not_require_command_or_test_count(self):
        self.contract['checks'] = [{'id': 'AC-1', 'expected': 'Both independent assertions hold.',
                                    'kinds': ['static'], 'execution': 'manual'}]
        check = self.report['checks'][0]
        check['kind'] = 'static'
        check['steps'] = ['Inspect the scoped file and record expected/actual in runner.log.']
        del check['execution']
        code, result = self.invoke(observations=False)
        self.assertEqual(code, 0, result)
        self.assertIn('does not prove claims', result['limitation'])

    def test_not_run_and_not_applicable_need_reason_and_remain_unmet(self):
        for verdict in ('Not Run', 'Not Applicable'):
            with self.subTest(verdict=verdict):
                self.report['checks'][0].update(verdict=verdict, reason='Required environment unavailable.')
                self.assert_blocked(f'required check is {verdict}')
        del self.report['checks'][0]['reason']
        code, result = self.invoke()
        self.assertEqual(code, 2, result)
        self.assertFalse(result['report_valid'])

    def test_duplicate_check_and_malformed_documents_fail_closed(self):
        self.report['checks'].append(copy.deepcopy(self.report['checks'][0]))
        code, result = self.invoke()
        self.assertEqual(code, 2, result)
        self.assertIn('duplicate check', result['errors'][0])
        self.report = []
        code, result = self.invoke()
        self.assertEqual(code, 2, result)
        self.assertFalse(result['report_valid'])

    def test_empty_acceptance_and_boolean_test_counts_are_invalid(self):
        self.contract['checks'] = []
        code, result = self.invoke()
        self.assertEqual(code, 2, result)
        self.contract['checks'] = [{'id': 'AC-1', 'expected': 'Both independent assertions hold.',
                                    'kinds': ['unit'], 'execution': 'command'}]
        self.report['checks'][0]['execution']['tests']['passed'] = True
        code, result = self.invoke()
        self.assertEqual(code, 2, result)

    def test_misspelled_acceptance_rule_is_rejected_instead_of_ignored(self):
        rule = self.contract['checks'][0]
        rule['minimum_test'] = rule.pop('minimum_tests')
        counts = {'total': 0, 'passed': 0, 'failed': 0, 'skipped': 0}
        self.report['checks'][0]['execution']['tests'] = counts
        self.observations['checks'][0]['execution']['tests'] = counts
        code, result = self.invoke()
        self.assertEqual(code, 2, result)
        self.assertIn('unknown acceptance field', result['errors'][0])

    def test_artifact_traversal_is_rejected_without_reading_outside_root(self):
        for path in ('../outside.log', '/absolute.log', 'C:/outside.log', 'folder\\outside.log'):
            with self.subTest(path=path):
                self.report['checks'][0]['artifacts'][0]['path'] = path
                code, result = self.invoke()
                self.assertEqual(code, 2, result)
                self.assertIn('unsafe artifact path', result['errors'][0])

    def test_report_commands_are_never_executed_by_checker(self):
        self.report['checks'][0]['execution']['command'] = [sys.executable, '-c',
            "from pathlib import Path; Path('must-not-exist').write_text('executed')"]
        self.assert_blocked('claimed execution differs from runner observation')
        self.assertFalse((self.root / 'must-not-exist').exists())


if __name__ == '__main__':
    unittest.main()
