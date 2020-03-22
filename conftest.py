"""
This is a standard pytest config file
"""
import pytest

from box import Box


@pytest.fixture(name="simple_box")
def simple_box_fixture():
    """
    Fixture to create a simple box with centre at 0,0 and dimensions 10,10
    """
    box = Box(0, 0)
    box.width = 10
    box.height = 10
    return box


@pytest.fixture(name="box_anchored_bottom_left")
def box_anchored_bottom_left_fixture():
    """
    Fixture to create a more complex box that has the following attributes:
    * Anchored bottom-left
    * positioned 10, 20
    * dimensions: 30, 40 (width, height)
    * text: "Exciting Box"
    """
    box = Box(10, 20)
    box.width = 30
    box.height = 40
    box.x_anchor = 0.0
    box.y_anchor = 0.0
    return box
