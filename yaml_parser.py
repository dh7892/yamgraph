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

def draw_deployments(data):
    """Find "deployments" in the data and draw them
    
    Args:
        data (List of dictionaries): the parsed yml data (list of dicts)
    """

    output_driver = OutputDriver("file")
    # look for elements of the list that have kind==Deployment
    deployments = []
    dep = Deployment("Steve")

    for section in data:
        if section.get("kind", "") == "Deployment":
            metadata = section.get("metadata", None)
            if metadata:
                name = metadata.get("name", None)
                if name:
                    deployments.append(Deployment(name))
                

    # for each deployment, draw a box with the name in it.
    for deployment in deployments:
        deployment.draw(output_driver)