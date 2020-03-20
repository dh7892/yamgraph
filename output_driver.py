"""
This module contains the code the actually produces graphics output.

The idea is that other parts of the code can make calls in here to draw
simple shapes and this will handle the job of actually converting that
to output in whatever format we've requested
"""
from colour import Colour

# Define some useful colour constants (we may move these later)
BACKGROUND_COLOUR = Colour("#FE8F80")


class OutputDriver:
    """
    This class can be used to do draw some simple shapes
    Each drawing operation will add the shape to a buffer.
    This will only be written to the file when output() is
    called. The idea of this is so that we don't 
    leave a file open for a while as we're putting in each
    shape. 
    """

    def __init__(self, filename, width=200, height=150):
        # Remember the canvas size in case we want to scale
        self.filename = filename
        self.width = width
        self.height = height

    def draw_box(self, start_x: int, start_y: int, width: int, height: int, colour: Colour):
        """Draw a box
        
        Args:
            start_x (int): The x position of the left side of the box
            start_y (int): The y position of the box (top or bottom TBC)
            width (int): The width of the box
            height (int): The height of the box
            colour (Colour): The colour of the background of the box
        Return: None
        """
        pass

    def output(self) -> None:
        """
        Write out the diagram to the filename specified.
        NOTE: all "drawing" should already have been done by calling other 
        methods first, to build up an image. This is the final step to output
        the image to a file.
        """
        print(f"This is where we will write a file for you!")
