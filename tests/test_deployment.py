"""
Unit tests for Deployment class
"""

import pytest

from deployment import Deployment

@pytest.mark.parametrize("name", ["Steve", "Bob"])
def test_create_deployment(name):
    """
    Test that we can create a deployment with the right name
    """
    deployment = Deployment(name)
    assert deployment.name == name