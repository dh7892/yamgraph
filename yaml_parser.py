"""This is a helper module that allows us to parse yml into objects
"""
from yaml import load_all


def read_yaml(data):
    """Read the yml data (stream) and return a generator of yaml data

    Args:
        data (str): A stream of data to paser (could be a string)
    """

    parsed_data = load_all(data)
    return list(parsed_data)
