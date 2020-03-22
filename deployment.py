"""This module contains the Deployment class
"""
from box import Box


class Deployment:
    """This class represents a k8s deployment
    """

    def __init__(self, name, box: Box = Box(0, 0)):
        self.name = name
        self.box = box

    def draw(self, driver):
        """Draw out our deployment to the driver provided

        Args:
            driver (OutputDriver): The driver that will handle the drawing commands
        """
        self.box.text = self.name
        self.box.draw(driver)
