"""
This file contains the command line parsing code
"""
import click

from output_driver import OutputDriver


@click.command()
@click.argument("output_file")
def process(output_file):
    print(f"Outputting to file: {output_file}")
    drawing = OutputDriver(output_file)
    drawing.draw_background("moo", 0, 0, 180, 90)
    drawing.output()


if __name__ == "__main__":
    process()
