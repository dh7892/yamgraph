"""
Unit tests for the command module
"""
from click.testing import CliRunner

from command import process


def test_simple_command():
    """
    Check a really simple invocation of the main command
    """
    result = CliRunner().invoke(process, ["example_yml/example1.yml", "output.svg"])
    # Check the command returned  success
    assert result.exit_code == 0
