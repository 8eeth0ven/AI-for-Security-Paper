"""Guard against realistic editing errors in a bilingual paper corpus."""
import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("catalog", Path(__file__).resolve().parents[1] / "scripts/build_catalog.py")
catalog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog)


class EditingErrors(unittest.TestCase):
    def setUp(self):
        self.original = catalog.ROOT
        self.temp = tempfile.TemporaryDirectory()
        catalog.ROOT = Path(self.temp.name)
        for lang, files in catalog.SOURCES.items():
            for name in files:
                target = catalog.ROOT / name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(self.original / name, target)

    def tearDown(self):
        catalog.ROOT = self.original
        self.temp.cleanup()

    def change(self, name, old, new):
        path = catalog.ROOT / name
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        path.write_text(text.replace(old, new, 1), encoding="utf-8")

    def test_duplicate_paper_is_rejected(self):
        path = catalog.ROOT / catalog.SOURCES["zh"][0]
        first = next(line for line in path.read_text(encoding="utf-8").splitlines() if line.startswith("| 1 |"))
        with path.open("a", encoding="utf-8") as f:
            f.write("\n" + first + "\n")
        with self.assertRaisesRegex(ValueError, "Duplicate ID"):
            catalog.load_language("zh")

    def test_dimension_sum_error_is_rejected(self):
        self.change(catalog.SOURCES["en"][0], "| 16 | 24 | 20 | 5 | 12 |", "| 16 | 23 | 20 | 5 | 12 |")
        with self.assertRaisesRegex(ValueError, "Score sum differs"):
            catalog.load_language("en")

    def test_master_score_drift_is_rejected(self):
        self.change(catalog.SOURCES["en"][1], "A / 77", "A / 78")
        with self.assertRaisesRegex(ValueError, "Master score differs"):
            catalog.load_language("en")

    def test_bilingual_date_drift_is_rejected(self):
        self.change(catalog.SOURCES["en"][1], "2026-01-27", "2026-01-28")
        with self.assertRaisesRegex(ValueError, "Bilingual date differs"):
            catalog.build()

    def test_missing_local_link_is_rejected(self):
        (catalog.ROOT / "README.md").write_text("[missing](absent.md)\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Broken local link"):
            catalog.check_links()

    def test_escaped_pipe_survives_export(self):
        papers = catalog.load_language("en")
        self.assertIn("curl|sh", papers["2610.29869"]["judgment"])


if __name__ == "__main__":
    unittest.main()
