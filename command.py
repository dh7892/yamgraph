"""
This file contains the command line parsing code
"""
import click

from yaml_parser import read_yaml, draw_deployments
from output_driver import OutputDriver


#@click.argument("input_file")
#@click.argument("output_file")
@click.command()
def process():
    """
    Handle command line arguements for main command
    """
    input_file = "example_yml/example1.yml"
    output_file = "test.ps"
    with open(input_file) as file:
        data = file.read()

    parsed_data = read_yaml(data)
    driver = OutputDriver(output_file)
    draw_deployments(parsed_data, driver)
    driver.output()


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    process()
