import subprocess
from unittest.mock import patch
import pytest
from plasmidhub.ani import run_fastani
from plasmidhub.abricate import run_abricate_bulk


@patch("subprocess.run")
def test_run_fastani_called(mock_run):
    mock_run.return_value.returncode = 0
    result = run_fastani("plasmid_list.txt")
    mock_run.assert_called()
    assert result is None or result == 0


@patch("subprocess.run")
def test_run_abricate_bulk_called(mock_run):
    mock_run.return_value.returncode = 0
    
    # Call with dummy inputs
    result = run_abricate_bulk(
        input_dir="test_data",
        results_dir="results",
        db_list=["resfinder", "ncbi"],
        threads=2
    )
    
    # Verify subprocess.run was called at least once
    mock_run.assert_called()
    assert result is None or result == 0