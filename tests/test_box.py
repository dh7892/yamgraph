"""
Unit tests for the Box class
"""
from unittest.mock import Mock


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
