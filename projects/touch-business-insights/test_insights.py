"""Run: python -m unittest discover -s projects/touch-business-insights -p 'test_*.py'"""
import tempfile
import unittest
from pathlib import Path
from insights import analyze, report


class InsightsTests(unittest.TestCase):
    def test_totals(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sales.csv"
            path.write_text("date,product,quantity,unit_price,unit_cost\n"
                            "2026-10-01,Cable,2,10000,6000\n"
                            "2026-10-02,Cable,1,10000,6000\n", encoding="utf-8")
            result = analyze(path)
            self.assertEqual(result["revenue"], 30000)
            self.assertEqual(result["profit"], 12000)
            self.assertEqual(result["units"], 3)
            self.assertIn("Cable", report(result))

    def test_reject_negative_quantity(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sales.csv"
            path.write_text("date,product,quantity,unit_price,unit_cost\n"
                            "2026-10-01,Cable,-2,10000,6000\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                analyze(path)


if __name__ == "__main__":
    unittest.main()
