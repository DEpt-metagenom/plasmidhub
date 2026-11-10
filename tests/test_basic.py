import importlib
import subprocess
from pathlib import Path


def test_import_modules():
    # Test import of core modules
    import plasmidhub.preprocessing
    import plasmidhub.ani
    import plasmidhub.clustering


def test_conda_environment_declares_bioconda_tooling():
    repo_root = Path(__file__).resolve().parents[1]
    env_text = (repo_root / "environment.yml").read_text()

    assert "bioconda" in env_text
    assert "fastani" in env_text
    assert "abricate" in env_text


def test_cli_version():
    result = subprocess.run(["plasmidhub", "--version"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "plasmidhub" in result.stdout.lower()
    assert "1.0.1" in result.stdout
