"""
Unit tests for Deployment class
"""

from unittest.mock import MagicMock, Mock

import pytest
from colour import Colour

from deployment import Deployment

BLACK = Colour("black")


@pytest.fixture(name="simple_deployment")
def simple_deployment_fixture(simple_box):
    """
    This fixture will return a simple Deployment
    with width 10, height 20, x_pos 5, y_pos 15, colour black
    and name "simple"
    """
    deployment = Deployment("simple", simple_box)
    return deployment


@pytest.mark.parametrize("name", ["Steve", "Bob"])
def test_create_deployment(name, simple_box):
    """
    Test that we can create a deployment with the right name
    """
    deployment = Deployment(name, simple_box)
    assert deployment.name == name


def test_draw(simple_deployment):
    """
    Test that a Deployment basically, we just want the deployment to
    call "draw" on its box
    """
    driver = Mock()
    simple_deployment.box.draw = MagicMock()

    simple_deployment.draw(driver)

    simple_deployment.box.draw.assert_called_once()
