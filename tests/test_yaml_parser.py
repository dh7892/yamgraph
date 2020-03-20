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


@mock.patch("output_driver.OutputDriver")
def test_draw_deployments(MockOutputDriver, simple_yml_data):
    """Test that we can draw a simple deployment
    """
    data = yaml_parser.read_yaml(simple_yml_data)
    yaml_parser.draw_deployments(data)

    # Check that we called "draw_box" once
    assert MockOutputDriver.draw_box.called