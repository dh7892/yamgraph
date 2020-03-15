"""
This file contains the command line parsing code
"""
import click


@click.command()
@click.argument("input_file")
def process(input_file):
    print(f"input file is: {input_file}")


if __name__ == "__main__":
    process()
