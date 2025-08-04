"""Test FastANI and ABRicate"""

import subprocess
from unittest.mock import patch, MagicMock
import pytest
from plasmidhub.ani import run_fastani
from plasmidhub.abricate import run_abricate_bulk


@patch("subprocess.run")
def test_run_fastani_called(mock_run):
    """Test that run_fastani calls subprocess.run and returns expected result."""
    mock_run.return_value.returncode = 0
    result = run_fastani("plasmid_list.txt")
    mock_run.assert_called()
    assert result is None or result == 0


@patch("subprocess.run")
@patch("pathlib.Path.glob")
def test_run_abricate_bulk_called(mock_glob, mock_run):
    """Test that run_abricate_bulk calls subprocess.run with mocked fasta files."""

    # Create a mock file object with a .name attribute
    mock_file = MagicMock()
    mock_file.name = "file1.fasta"

    # Define a side_effect function to return different results depending on glob pattern
    def glob_side_effect(pattern):
        if pattern == "*.fna":
            return []
        elif pattern == "*.fa":
            return []
        elif pattern == "*.fasta":
            return [mock_file]
        else:
            return []

    mock_glob.side_effect = glob_side_effect
    mock_run.return_value.returncode = 0

    result = run_abricate_bulk(
        input_dir="test_data",
        results_dir="results",
        db_list=["resfinder", "ncbi"],
        threads=2,
    )

    mock_run.assert_called()
    assert result is None or result == 0
