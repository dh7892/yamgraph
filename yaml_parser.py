"""This is a helper module that allows us to parse yml into objects
"""
from yaml import load_all

from output_driver import OutputDriver, BACKGROUND_COLOUR
from deployment import Deployment


def read_yaml(data):
    """Read the yml data (stream) and return a generator of yaml data

    Args:
        data (str): A stream of data to paser (could be a string)
    """

    parsed_data = load_all(data)
    return list(parsed_data)

def draw_deployments(data, driver):
    """Find "deployments" in the data and draw them
    
    Args:
        data (List of dictionaries): the parsed yml data (list of dicts)
        driver: the output driver to use
    """

                


def get_deployments(data):
    """
    Look through the data and pull out a list of deployment objects
    from it

    Args:
      data: the parsed yaml data (nested lists and dicts)
    
    Returns:
      A list of Deployment objects
    """

    # look for elements of the list that have kind==Deployment
    deployments = []

    for section in data:
        if section.get("kind", "") == "Deployment":
            metadata = section.get("metadata", None)
            if metadata:
                name = metadata.get("name", None)
                if name:
                    deployments.append(Deployment(name))

    return deployments