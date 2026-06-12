import subprocess
import sys

def run_cmd(intent):
    result = subprocess.run(
        [sys.executable, "query.py", intent],
        capture_output=True,
        text=True
    )
    return result


def test_select_intent():
    result = run_cmd("list authors at neurips")
    assert "SELECT" in result.stdout
    assert result.returncode == 0


def test_ask_intent():
    result = run_cmd("is ai research available")
    assert "ASK" in result.stdout
    assert result.returncode == 0


def test_construct_intent():
    result = run_cmd("citation graph")
    assert "CONSTRUCT" in result.stdout
    assert result.returncode == 0


def test_unknown_intent():
    result = run_cmd("random intent")
    assert result.returncode != 0
    assert "Unknown intent" in result.stdout