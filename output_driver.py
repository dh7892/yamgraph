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
        self.buffer = """%!PS
% Function to draw centred text
/cshow { dup stringwidth pop -0.5 mul 0 rmoveto show } def

% Make the background white
newpath
0 0 moveto
0 500 lineto
500 500 lineto
500 0 lineto
closepath
1 1 1 setrgbcolor
fill
"""

    def draw_box(
        self, start_x: int, start_y: int, end_x: int, end_y: int, colour: Colour
    ):
        """Draw a box

        Args:
            start_x (int): The x position of the left side of the box
            start_y (int): The y position of the bottom
            end_x (int): The x position of the right side
            end_y (int): The y position of the top
            colour (Colour): The colour of the background of the box
        Return: None
        """
        red, blue, green = colour.rgb()
        self.buffer += f"""
newpath
{start_x} {start_y} moveto
{start_x} {end_y} lineto
{end_x} {end_y} lineto
{end_x} {start_y} lineto
closepath
gsave
{red} {blue} {green} setrgbcolor
fill
grestore

0 setgray
2 setlinewidth
0 0 0 setrgbcolor
stroke
"""

    def draw_text(self, text: str, x_pos, y_pos):
        """
        Draw the text, centred on x_pos, y_pos

        Args:
          text: The text to draw
          x_pos; The x coordinate of the centre of the text
          y_pos; The y coordinate of the centre of the text
        """
        self.buffer += f"""
/Times-Roman findfont 10 scalefont setfont
{x_pos} {y_pos} moveto 0 0 0 setrgbcolor ({text}) cshow
"""

    def output(self) -> None:
        """
        Write out the diagram to the filename specified.
        NOTE: all "drawing" should already have been done by calling other
        methods first, to build up an image. This is the final step to output
        the image to a file.
        """
        with open(self.filename, "w") as file:
            file.write(self.buffer)
