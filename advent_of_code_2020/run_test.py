import os
from click.testing import CliRunner

from advent_of_code_2020 import run

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
INPUT_FILE = os.path.join(ROOT_DIR, "day_1a", "sample_input.txt")


def test_day_1a() -> None:
    runner = CliRunner()
    result = runner.invoke(run.day1, ["--input-file", INPUT_FILE])
    assert result.exit_code == 0, result.output
    assert result.output.strip() == str(514_579), result.output
