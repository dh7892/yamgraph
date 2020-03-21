"""This module contains the Deployment class
"""
from output_driver import BACKGROUND_COLOUR


class Deployment:
    """This class represents a k8s deployment
    """

    def __init__(self, name):
        self.name = name
        self.x_pos = 0
        self.y_pos = 0
        self.width = 10
        self.height = 10
        self.colour = BACKGROUND_COLOUR

    def draw(self, driver):
        """Draw out our deployment to the driver provided

        Args:
            driver (OutputDriver): The driver that will handle the drawing commands
        """
        driver.draw_box(self.x_pos, self.y_pos, self.width, self.height, self.colour)
