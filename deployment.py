"""This module contains the Deployment class
"""
from colour import Colour

from box import Box

# Constant for the size of a small box (like for controller type)
SMALL_BOX_SIZE = 10

DEPLOYMENT_COLOUR = Colour("#CEE8AD")
CONTAINER_COLOUR = Colour("#A3D977")
COMPUTE_COLOUR = Colour("#7BB54B")
NETWORK_COLOUR = Colour("#FFEDAB")
CONFIG_COLOUR = Colour("#9AD2F1")
VOLUME_COLOUR = Colour("#9BD1F3")


class Deployment:
    """This class represents a k8s deployment
    """

    def __init__(self, name, box: Box = Box(0, 0, min_width=160, min_height=120)):
        self.name = name
        self.box = box
        self._containers = []
        self._controller_type = "D"
        self._controller_cardinality = 1
        self._config_managements = []
        self._newwork_configs = []
        self._storage_configs = []

    def draw(self, driver):
        """Draw out our deployment to the driver provided

        Args:
            driver (OutputDriver): The driver that will handle the drawing commands
        """
        # Draw the main box
        self.box.text = self.name
        self.box.colour = DEPLOYMENT_COLOUR
        self.box.draw(driver)

        # Draw the controller stuff on the left
        x_pos = self.box.left
        y_pos = self.box.top - self.box.height / 5.0
        label_box = Box(
            x_pos,
            y_pos,
            text=self._controller_type,
            min_height=SMALL_BOX_SIZE * 2,
            min_width=SMALL_BOX_SIZE * 3,
        )
        label_box.colour = COMPUTE_COLOUR
        # Anchor the label box on the right so it will sit next to the main box
        label_box.x_anchor = 1.0
        # Now we can draw the box
        label_box.draw(driver)

        # Draw the cardinality
        # We can re-use the box but change only what's different
        label_box.text = f"{self._controller_cardinality}"
        label_box.y_pos = self.box.bottom + self.box.height / 5.0
        # And draw it.
        label_box.draw(driver)

    def add_container(self, container):
        """
        Add a container to the Pod
        """

    def bounding_box(self) -> Box:
        """
        Return a Box that represents the bounding box for the object, including the
        stuff on the sides
        """
        left = self.box.left - SMALL_BOX_SIZE
        # We will add on to these numbers when we add stuff on to the sides
        right = self.box.right
        bottom = self.box.bottom
        top = self.box.top

        box = Box(left, right)
        box.width = right - left
        box.height = top - bottom
        return box
