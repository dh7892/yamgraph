"""
This module contains the the base class for an output driver.
The idea is that we can specialise this class to provide output in different image
formats
"""
import cairo


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

        filetype = self.filename.split(".")[-1]
        # Standard cairo setup
        if filetype == "svg":
            self.surface = cairo.SVGSurface(self.filename, self.width, self.height)
        else:
            raise ValueError(f"Don't know how to output the file {self.filename}")

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
        ctx = cairo.Context(self.surface)
        pat = cairo.SolidPattern(*self.background_colour)
        ctx.rectangle(x, y, width, height)
        ctx.set_source(pat)
        ctx.fill()
        ctx.stroke()

    def output(self) -> None:
        """
        Write out the diagram to the filename specified.
        NOTE: all "drawing" should already have been done by calling other methods first, to build up an image. This
        is the final step to output the image to a file.
        :param filename: The name of the file to write to
        :param filetype: The type of file to write (e.g. "svg")
        :return: None
        """
        self.surface.show_page()
