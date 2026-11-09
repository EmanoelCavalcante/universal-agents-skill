import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable

class ScriptsTests(unittest.TestCase):
    def test_catalog(self):
        data = json.loads((ROOT/'CATALOGO.json').read_text(encoding='utf-8'))
        self.assertEqual(data['total'], 17)

    def test_validate(self):
        r = subprocess.run([PYTHON, str(ROOT/'scripts/validate_skills.py')], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_install_and_preserve(self):
        with tempfile.TemporaryDirectory() as t:
            target = Path(t)
            args = [PYTHON, str(ROOT/'scripts/install_skills.py'), '--agent', 'codex', '--scope', 'project', '--target', str(target), '--skill', 'mentoria-programacao']
            r = subprocess.run(args, capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stdout+r.stderr)
            file = target / '.agents/skills/mentoria-programacao/SKILL.md'
            self.assertTrue(file.exists())
            file.write_text('Conteúdo próprio', encoding='utf-8')
            r = subprocess.run(args, capture_output=True, text=True)
            self.assertEqual(r.returncode, 0)
            self.assertEqual(file.read_text(encoding='utf-8'), 'Conteúdo próprio')

    def test_zip(self):
        with tempfile.TemporaryDirectory() as t:
            r = subprocess.run([PYTHON, str(ROOT/'scripts/package_skills.py'), '--skill', 'mentoria-programacao', '--out', t], capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stdout+r.stderr)
            with zipfile.ZipFile(Path(t)/'mentoria-programacao.zip') as z:
                self.assertIn('mentoria-programacao/SKILL.md', z.namelist())

if __name__ == '__main__':
    unittest.main()
