"""Test FastANI and ABRicate"""

import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

from plasmidhub.abricate import change_dir, run_abricate_bulk
from plasmidhub.ani import run_fastani


@patch("subprocess.run")
def test_run_fastani_called(mock_run):
    """Test that run_fastani calls subprocess.run and returns expected result."""
    mock_run.return_value.returncode = 0
    result = run_fastani("plasmid_list.txt")
    mock_run.assert_called()
    assert result is None or result == 0


@patch("subprocess.run")
def test_run_fastani_builds_expected_command(mock_run):
    mock_run.return_value.returncode = 0

    run_fastani(
        "plasmid_list.txt",
        fragLen=500,
        minFrag=7,
        kmer=17,
        output_dir="results",
        threads=8,
    )

    cmd = mock_run.call_args[0][0]
    assert cmd[:5] == ["fastANI", "--ql", "plasmid_list.txt", "--rl", "plasmid_list.txt"]
    assert "--fragLen" in cmd
    assert "--minFraction" in cmd
    assert "--kmer" in cmd
    assert "-t" in cmd
    assert "8" in cmd


@patch("subprocess.run")
def test_run_abricate_bulk_called_with_temp_dirs(mock_run):
    """Test run_abricate_bulk using real temporary directories and a dummy fasta file."""
    mock_run.return_value.returncode = 0

    with tempfile.TemporaryDirectory() as tmp_input_dir, tempfile.TemporaryDirectory() as tmp_results_dir:
        # Create a dummy fasta file in the temporary input directory
        dummy_fasta = Path(tmp_input_dir) / "file1.fasta"
        dummy_fasta.write_text(">seq1\nATCG")

        result = run_abricate_bulk(
            input_dir=tmp_input_dir,
            results_dir=tmp_results_dir,
            db_list=["resfinder", "ncbi"],
            threads=2,
        )

        mock_run.assert_called()
        assert result is None or result == 0


def test_change_dir_restores_original_working_directory(tmp_path):
    original_dir = Path.cwd()

    with change_dir(tmp_path):
        assert Path.cwd() == tmp_path.resolve()

    assert Path.cwd() == original_dir


def test_run_abricate_bulk_raises_for_missing_fasta_files(tmp_path):
    results_dir = tmp_path / "results"

    with pytest.raises(RuntimeError, match="No input files found"):
        run_abricate_bulk(str(tmp_path), str(results_dir), ["resfinder"])

