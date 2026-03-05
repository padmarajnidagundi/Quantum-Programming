import subprocess
import sys
from pathlib import Path
import unittest


class TestSimpleHadamardMeasure(unittest.TestCase):
    def test_script_runs_and_prints_results(self):
        script_path = Path(__file__).resolve().parents[1] / "Cirq" / "simple_hadamard_measure.py"

        completed = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            check=True,
        )

        self.assertIn("Results of measuring a Hadamard-applied qubit:", completed.stdout)
        self.assertIn("result=", completed.stdout)


if __name__ == "__main__":
    unittest.main()