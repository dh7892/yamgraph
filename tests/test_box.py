"""
Unit tests for the Box class
"""
import pytest

from box import Box


@pytest.fixture(name="simple_box")
def simple_box_fixture():
    """
    Fixture to create a simple box with centre at 0,0 and dimensions 10,10
    """
    return Box(0, 0, width=10, height=10)


@pytest.fixture(name="box_anchored_bottom_left")
def box_anchored_bottom_left_fixture():
    """
    Fixture to create a more complex box that has the following attributes:
    * Anchored bottom-left
    * positioned 10, 20
    * dimensions: 30, 40 (width, height)
    * text: "Exciting Box"
    """
    box = Box(10, 20, width=30, height=40)
    box.x_anchor = 0.0
    box.y_anchor = 0.0
    return box


def test_simple_box(simple_box):
    """
    Just kickin' the tyres on a Box
    """
    assert simple_box.bottom == -5
    assert simple_box.left == -5
    assert simple_box.top == 5
    assert simple_box.right == 5


def test_exciting_box(box_anchored_bottom_left):
    """
    Checkin' out a more exciting box
    """
    width = box_anchored_bottom_left.width
    height = box_anchored_bottom_left.height
    assert box_anchored_bottom_left.left == box_anchored_bottom_left.x_pos
    assert box_anchored_bottom_left.bottom == box_anchored_bottom_left.y_pos
    assert box_anchored_bottom_left.right == box_anchored_bottom_left.x_pos + width
    assert box_anchored_bottom_left.top == box_anchored_bottom_left.y_pos + height
