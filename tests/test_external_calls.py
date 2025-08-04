import subprocess
from unittest.mock import patch
import pytest
from plasmidhub.ani import run_fastani  # example function calling fastANI

@patch("subprocess.run")
def test_run_fastani_called(mock_run):
    # Setup mock return value
    mock_run.return_value.returncode = 0

    # Call the function (adapt to your actual function signature)
    result = run_fastani(["query.fasta", "ref.fasta"])

    # Check subprocess.run was called
    mock_run.assert_called()

    # Check return or side effects if any
    assert result is None or result == 0  # depending on your function
