"""
This file contains the command line parsing code
"""
import click

from output_driver import OutputDriver
from yaml_parser import get_deployments, read_yaml


@click.command()
@click.argument("input_file")
@click.argument("output_file")
def process(input_file, output_file):
    """
    Handle command line arguements for main command
    """
    with open(input_file) as file:
        data = file.read()

    parsed_data = read_yaml(data)
    deployments = get_deployments(parsed_data)

    driver = OutputDriver(output_file)
    # for each deployment, draw a box with the name in it.
    # Draw each box and add 10 to each used x,y coordinate- check  syntax to do this
    spacing = 10
    for index, deployment in enumerate(deployments):
        deployment.x_pos = index * spacing
        deployment.draw(driver)
    driver.output()


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    process()
