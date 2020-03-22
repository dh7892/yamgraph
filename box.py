"""
This module contains a Box class
"""

from colour import Colour


def _text_width(text: str) -> int:
    """
    Return the width that this text takes up
    """
    # TODO #1, take account of the fact that the text may be split into lines
    char_width = 5
    return len(text) * char_width


def _text_height(text: str) -> int:
    """
    Return the width that this text takes up
    """
    char_height = 5
    lines = len(text.split("\n"))
    return lines * char_height


class Box:
    """
    The Box class is just what it says on the tin; it's a box!
    """

    def __init__(
        self,
        x_pos: int,
        y_pos: int,
        text: str = "",
        min_width: int = 10,
        min_height: int = 10,
    ):
        """
        Create a Box

        Args:
          x_pos: The x position of the box
          y_pos: The y position of the box
          text: The text to show in the box
          min_width: The minimum width for the box
          min_height: The minimum height for the box
        """
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.colour = Colour("black")

        # These settings are ratios of how far up/across our anchor point
        # is (0 => left, 0.5 => middle, 1 => right for x)
        self.x_anchor = 0.5
        self.y_anchor = 0.5

        self._min_width = min_width
        self._min_height = min_height

        # Setting the text will actually try to resize the box so we need to
        # do this last to make sure the min and max have already been set
        self.text = text

    @property
    def width(self) -> int:
        """
        The width of the box
        """
        return self._width

    @width.setter
    def width(self, value: int) -> None:
        """
        Set the width but protect minimum
        """
        self._width = max(self._min_width, value)

    @property
    def height(self) -> int:
        """
        The height of the box
        """
        return self._height

    @height.setter
    def height(self, value: int) -> None:
        """
        Set the height but protect minimum
        """
        self._height = max(self._min_height, value)

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

    @property
    def text(self) -> str:
        """
        Get the text displayed in the box
        """
        return self._text

    @text.setter
    def text(self, text: str) -> None:
        """
        Setter for the text. Will try to resize the box to fit
        """
        self._text = text
        self.width = _text_width(text)
        self.height = _text_height(text)

    def draw(self, driver):
        """
        Draw the box using the output driver provided
        """
        driver.draw_box(self.left, self.bottom, self.right, self.top, self.colour)
