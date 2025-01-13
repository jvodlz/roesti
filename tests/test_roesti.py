from typer.testing import CliRunner
from roesti.roesti import app, get_digest, configure_file_path
from unittest.mock import patch

runner = CliRunner()

def test_display_hash_type():
    result = runner.invoke(app, "display-hash-types")
    assert result.exit_code == 0
    assert "[ 5 ] sha512" in result.stdout

def test_display_hash_modes():
    result = runner.invoke(app, "display-hash-modes")
    assert result.exit_code == 0
    assert "[ 2 ]" in result.stdout

def test_get_hash(tmp_path):
    temp_file = tmp_path / "dummy.txt"
    temp_file.write_text("This is a hash gen test")
    result = runner.invoke(app, ["generate-file-hash", str(temp_file), "sha256"])
    assert result.exit_code == 0
    assert "Reading..." in result.stdout
    assert "0:00:00" in result.stdout

def test_get_digest():
    dummy_hash = "  3119220EEE88548be48efc060888697bd7ed40557613cb955c23659450345516  "
    expected_hash = "3119220eee88548be48efc060888697bd7ed40557613cb955c23659450345516"
    with patch("builtins.input", return_value=dummy_hash):
        result = get_digest()
        assert result == expected_hash

def test_configure_file_path_whitespace(tmp_path):
    # tmp_path autocleans after test completion
    
    temp_file = tmp_path / "dummy.txt"
    temp_file.touch()
    expected_out = str(temp_file)
    input_path = f" {temp_file}   "
    with patch("builtins.input", return_value=input_path):
        result = configure_file_path()
        assert result == expected_out
