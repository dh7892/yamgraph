"""
This file contains the command line parsing code
"""
import click

from yaml_parser import read_yaml
from output_driver import OutputDriver


@click.command()
@click.argument("input_file")
@click.argument("output_file")
def process(input_file, output_file):
    """
    Handle command line arguements for main command
    """
    with open(input_file) as file:
        data = file.read()

    read_yaml(data)
    print(f"Outputting to file: {output_file}")
    drawing = OutputDriver(output_file)
    drawing.output()


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    process()
