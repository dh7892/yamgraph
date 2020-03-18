"""
Unit tests for the command module
"""
import pytest
from click.testing import CliRunner

from command import process

def test_simple_command():
    """
    Check a really simple invokation of the main command
    """
    result = CliRunner().invoke(process, ["output.svg"])
    # Check the command returned  succes
    assert result.exit_code == 0


