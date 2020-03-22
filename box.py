"""
This module contains a Box class
"""

from colour import Colour


class Box:
    """
    The Box class is just what it says on the tin; it's a box!
    """

    def __init__(
        self, x_pos: int, y_pos: int, width: int = 10, height: int = 10, text: str = ""
    ):
        """
        Create a Box

        Args:
          x_pos: The x position of the box
          y_pos: The y position of the box
          width: The width of the box
          height: The height of the box
          text: The text to show in the box
        """
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.text = text
        self.colour = Colour("black")

        # These settings are ratios of how far up/across our anchor point
        # is (0 => left, 0.5 => middle, 1 => right for x)
        self.x_anchor = 0.5
        self.y_anchor = 0.5

    @property
    def left(self):
        """
        The x coord of the left of the box
        """
        return int(float(self.x_pos) - (float(self.width) * float(self.x_anchor)))

    @property
    def right(self):
        """
        The x coord of the right of the box
        """
        return self.left + self.width

    @property
    def bottom(self):
        """
        The y coord of the bottom of the box
        """
        return int(float(self.y_pos) - (float(self.height) * float(self.y_anchor)))

    @property
    def top(self):
        """
        The y coord of the top of the box
        """
        return self.bottom + self.height

    def draw(self, driver):
        """
        Draw the box using the output driver provided
        """
        driver.draw_box(self.left, self.bottom, self.right, self.top, self.colour)
