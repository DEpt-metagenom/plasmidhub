import logging
import os

import pytest
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

from plasmidhub.preprocessing import (
    validate_and_list_plasmids,
    validate_sequence_content,
    write_plasmid_list,
    write_plasmid_sizes,
)


def test_validate_and_list_plasmids(tmp_path):
    # Create a valid FASTA file
    valid_fasta = tmp_path / "valid_plasmid.fasta"
    valid_fasta.write_text(">plasmid1\nACTGACTGACTG\n")

    # Create an invalid FASTA file (empty)
    invalid_fasta = tmp_path / "invalid_plasmid.fasta"
    invalid_fasta.write_text("")

    # Create a non-FASTA file (wrong extension)
    other_file = tmp_path / "notes.txt"
    other_file.write_text("This is not a fasta")

    plasmid_files = validate_and_list_plasmids(str(tmp_path))

    # Should find only the valid FASTA file
    assert len(plasmid_files) == 1
    assert os.path.basename(plasmid_files[0]) == "valid_plasmid.fasta"


def test_validate_sequence_content_warns_on_invalid_nucleotides(caplog):
    records = [SeqRecord(Seq("ACGTX"), id="bad")]

    with caplog.at_level(logging.WARNING):
        validate_sequence_content(records, "bad.fasta")

    assert "non-standard nucleotides" in caplog.text
    assert "X" in caplog.text


def test_write_plasmid_list_and_sizes(tmp_path):
    fasta_one = tmp_path / "plasmid_1.fasta"
    fasta_two = tmp_path / "plasmid_2.fa"
    fasta_one.write_text(">seq1\nACGT\n")
    fasta_two.write_text(">seq2\nAAAA\nTTTT\n")

    plasmid_files = [str(fasta_one), str(fasta_two)]
    plasmid_list_out = tmp_path / "plasmid_list.txt"
    sizes_out = tmp_path / "plasmid_sizes.txt"

    write_plasmid_list(plasmid_files, output_file=str(plasmid_list_out))
    write_plasmid_sizes(plasmid_files, output_file=str(sizes_out))

    assert plasmid_list_out.read_text().splitlines() == plasmid_files
    assert sizes_out.read_text().splitlines() == [
        "PlasmidID\tSize",
        "plasmid_1.fasta\t4",
        "plasmid_2.fa\t8",
    ]