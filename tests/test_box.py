"""
Unit tests for the Box class
"""
from unittest.mock import Mock

import pytest

from box import Box


def test_simple_box(simple_box):
    """
    Just kicking the tyres on a Box
    """
    assert simple_box.bottom == -5
    assert simple_box.left == -5
    assert simple_box.top == 5
    assert simple_box.right == 5


def test_exciting_box(box_anchored_bottom_left):
    """
    Checking out a more exciting box
    """
    width = box_anchored_bottom_left.width
    height = box_anchored_bottom_left.height
    assert box_anchored_bottom_left.left == box_anchored_bottom_left.x_pos
    assert box_anchored_bottom_left.bottom == box_anchored_bottom_left.y_pos
    assert box_anchored_bottom_left.right == box_anchored_bottom_left.x_pos + width
    assert box_anchored_bottom_left.top == box_anchored_bottom_left.y_pos + height


def test_draw(simple_box):
    """
    Test that a Box will hit the expected expected calls
    in the output driver.
    """
    driver = Mock()

    simple_box.draw(driver)

    driver.draw_box.assert_called_once_with(-5, -5, 5, 5, simple_box.colour)


@pytest.mark.parametrize(
    ("width", "height", "expected_width", "expected_height"),
    [(10, 10, 10, 10), (5, 5, 10, 10), (15, 15, 15, 15)],
)
def test_mimimum_dimensions(width, height, expected_width, expected_height, simple_box):
    """
    Test that attempts to set the width and height will not violate min constraints
    """
    simple_box.width = width
    simple_box.height = height
    assert simple_box.width == expected_width
    assert simple_box.height == expected_height


@pytest.fixture(name="four_boxes")
def four_boxes_fixture():
    """
    Return 4 boxes with increasingly large text
    """
    box1 = Box(
        0, 0, text="a"
    )  # One char name so shouldn't be smaller than min width/height
    box2 = Box(0, 0, text="Small")
    box3 = Box(0, 0, text="Bigger than 10")
    box4 = Box(0, 0, text="Really, really big box")
    return box1, box2, box3, box4


def test_setting_text_sets_box_size(four_boxes):
    """
    Check that setting the text will change the size of the box
    """
    box1, box2, box3, box4 = four_boxes
    # Now test that the boxes increase in width
    assert box1.width < box2.width
    assert box2.width < box3.width
    assert box3.width < box4.width
