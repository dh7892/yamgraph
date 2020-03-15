"""
This module contains the class for the SVG output driver
"""
import drawSvg as draw
from output_driver import OutputDriver
from typing import IO

class SvgOutputDriver(OutputDriver):
    """
    A concrete OutputDriver that writes SVG files
    """
    def __init__(self):
        self.buffer = draw.Drawing(200, 100, origin="center")

    def draw_background(self, name: str, width: int, height: int) -> None:
        self.buffer.append(draw.Rectangle(0, 0, 180, 90, fill="#FE8F80"))

    def output(self, filename: str) -> None:
        self.buffer.saveSvg(filename)
