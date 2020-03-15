"""
This file contains the command line parsing code
"""
import click

from svg_driver import SvgOutputDriver


@click.command()
@click.argument("output_file")
def process(output_file):
    print(f"Outputting to file: {output_file}")
    drawing = SvgOutputDriver()
    drawing.draw_background(180, 90, "Moo")
    drawing.output(output_file)


if __name__ == "__main__":
    process()
