"""
Unit tests for yaml_parser
"""

import pytest
import tempfile
from unittest import mock

import yaml_parser

@pytest.fixture
def simple_yml_data():
    """Return some simple yml
    """
    data =  """
apiVersion: v1
kind: Service
    """
    return data

@pytest.fixture
def yml_with_deployments():
    """Return name of each thing that has kind = Deployment and add to a list
    """
    # Format should come from MetaData: Name: and print a list of these names
    data ="""---
apiVersion: v1
kind: Deployment
MetaData:
   Name: Bear
---
apiVersion: v1
kind: Deployment
MetaData:
   Name: Goat

    """
    return data

@pytest.fixture
def empty_data():
    return ""

def test_read_yaml_simple(simple_yml_data):
    """Check we can read a simple yml and get data
    """
    data = yaml_parser.read_yaml(simple_yml_data)
    # Convert to a list
    assert len(data) == 1
    assert data[0]["apiVersion"] == "v1"
    assert data[0]["kind"] == "Service"

def test_empty_data(empty_data):
    """Test that we gracefully get an empty list of data if we feed an empty
    string to the function
    """


@mock.patch("output_driver.OutputDriver.draw_box")
def test_draw_deployments_no_deployment(MockDrawBox, simple_yml_data):
    """Test that don't draw anything if we don't have any deployments to draw
    """
    data = yaml_parser.read_yaml(simple_yml_data)
    yaml_parser.draw_deployments(data)

    # Check that we called "draw_box" no times
    assert MockDrawBox.call_count == 0

@mock.patch("output_driver.OutputDriver.draw_box")
def test_draw_deployments(MockDrawBox, yml_with_deployments):
    """Test that we draw two boxes for our two deployments
    """
    data = yaml_parser.read_yaml(yml_with_deployments)
    yaml_parser.draw_deployments(data)

    # Check that we called "draw_box" twice
    assert MockDrawBox.call_count == 2