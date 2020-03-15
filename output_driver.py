"""
This module contains the the base class for an output driver.
The idea is that we can specialise this class to provide output in different image
formats
"""
from abc import ABC, abstractmethod
from typing import IO

class OutputDriver(ABC):
    """
    This base class provides the interface for all other output drivers to follow.

    OutputDriver classes will always write to an internal buffer when draw commmands are invoked.
    To send the data to an actual file, use the `output` method.
    """
    @abstractmethod
    def draw_background(self, name: str, width: int, height: int) -> None:
        """
        Draw the standard background for the diagram, this is an orange box with the name of the cluster in it
        :param name: The name to put inside the box
        :param width: The width of the box (pixels)
        :param height: The height of the box (pixels)
        :return: None
        """
        pass

    @abstractmethod
    def output(self, filename: str) -> None:
        """
        Write out the diagram to the filename specified.
        NOTE: all "drawing" should already have been done by calling other methods first, to build up an image. This
        is the final step to output the image to a file.
        :param filename: The name of the file to write to
        :return: None
        """
        pass
