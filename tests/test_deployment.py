"""
Unit tests for Deployment class
"""

import pytest
from unittest.mock import Mock
from colour import Colour


from deployment import Deployment

BLACK = Colour("black")

@pytest.fixture(name="simple_deployment")
def simple_deployment_fixture():
    """
    This fixture will return a simple Deployment
    with width 10, height 20, x_pos 5, y_pos 15, colour black
    and name "simple"
    """
    deployment = Deployment("simple")
    deployment.x_pos = 5
    deployment.y_pos = 15
    deployment.width = 10
    deployment.height = 20
    deployment.colour = BLACK
    return deployment

@pytest.mark.parametrize("name", ["Steve", "Bob"])
def test_create_deployment(name):
    """
    Test that we can create a deployment with the right name
    """
    deployment = Deployment(name)
    assert deployment.name == name

def test_draw(simple_deployment):
    """
    Test that a Deployment will hit the expected expected calls
    in the output driver.
    """
    driver = Mock()

    simple_deployment.draw(driver)

    driver.draw_box.assert_called_once_with(5, 15, 10, 20, BLACK)