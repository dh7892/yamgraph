"""
Unit tests for Deployment class
"""

import pytest

from deployment import Deployment

def test_create_deployment():
    """
    Test that we can create a deployment with the right name
    """
    name = "Steve"
    deployment = Deployment(name)
    assert deployment.name == name