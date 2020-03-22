"""This is a helper module that allows us to parse yml into objects
"""
from yaml import Loader, load_all

from deployment import Deployment


def read_yaml(data):
    """Read the yml data (stream) and return a generator of yaml data

    Args:
        data (str): A stream of data to parse (could be a string)
    """

    parsed_data = load_all(data, Loader=Loader)
    return list(parsed_data)


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
