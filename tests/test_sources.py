"""Validate source integrity without inventing Git history for workspace captures."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

REPO = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('skills_tool', REPO / 'tools/skills.py')
SKILLS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SKILLS)


class SourceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='skill-source-test-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for directory in ('skills', 'sources'):
            shutil.copytree(REPO / directory, self.root / directory)
        shutil.copy2(REPO / 'catalog.json', self.root / 'catalog.json')
        self.manifest_path = self.root / 'sources/manifest.json'
        self.manifest = json.loads(self.manifest_path.read_text(encoding='utf-8'))
        self.und = next(source for source in self.manifest['sources'] if source['id'] == 'und')

    def validate(self):
        self.manifest_path.write_text(json.dumps(self.manifest), encoding='utf-8')
        with patch.object(SKILLS, 'ROOT', self.root), contextlib.redirect_stdout(io.StringIO()):
            SKILLS.validate()

    def test_git_and_workspace_sources_validate_together(self):
        self.validate()

    def test_workspace_capture_cannot_claim_git_identity(self):
        self.und['commit'] = 'a' * 40
        with self.assertRaisesRegex(ValueError, 'must not claim'):
            self.validate()

    def test_capture_needs_an_origin_and_date(self):
        del self.und['captured_on']
        with self.assertRaisesRegex(ValueError, 'capture date and origin'):
            self.validate()

    def test_invalid_git_commit_is_still_rejected(self):
        self.manifest['sources'][0]['commit'] = None
        with self.assertRaisesRegex(ValueError, 'Invalid source commit'):
            self.validate()

    def test_changed_workspace_bytes_are_rejected(self):
        snapshot = self.root / self.und['files'][0]['snapshot_path']
        snapshot.write_bytes(snapshot.read_bytes() + b'changed\n')
        with self.assertRaisesRegex(ValueError, 'Snapshot hash mismatch'):
            self.validate()

    def test_unrecorded_workspace_file_is_rejected(self):
        (self.root / 'sources/und/extra.txt').write_text('unrecorded', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'inventory differs'):
            self.validate()


if __name__ == '__main__':
    unittest.main()
