"""
This module contains the the base class for an output driver.
The idea is that we can specialise this class to provide output in different image
formats
"""


class OutputDriver:
    """
    This class can be used to do all of the drawing
    """

    # Define some useful colours that we can use in any driver.
    background_colour = (x/255 for x in (254, 143, 128))

    def __init__(self, filename, width=200, height=150):
        # Remember the canvas size in case we want to scale
        self.filename = filename
        self.width = width
        self.height = height

    def draw_background(self, name: str, x: int, y: int, width: int, height: int) -> None:
        """
        Draw the standard background for the diagram, this is an orange box with the name of the cluster in it
        :param name: The name to put inside the box
        :param x: The x-coord of the box
        :param y: The y-coord of the box
        :param width: The width of the box (pixels)
        :param height: The height of the box (pixels)
        :return: None
        """
        pass

    def output(self) -> None:
        """
        Write out the diagram to the filename specified.
        NOTE: all "drawing" should already have been done by calling other methods first, to build up an image. This
        is the final step to output the image to a file.
        :param filename: The name of the file to write to
        :param filetype: The type of file to write (e.g. "svg")
        :return: None
        """
        print(f"This is where we will write a file for you!")
