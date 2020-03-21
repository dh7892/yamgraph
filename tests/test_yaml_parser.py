"""
Unit tests for yaml_parser
"""

import pytest
import tempfile

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
    """Return some yml that has two deployments: Bear and Goat
    """
    # Format should come from MetaData: Name: and print a list of these names
    data ="""---
apiVersion: v1
kind: Deployment
metadata:
   name: Bear
---
apiVersion: v1
kind: Deployment
metadata:
   name: Goat

    """
    return data

@pytest.fixture
def yml_with_no_metadata():
    """Return some yml that doesn't have any "MetaData"
    """
    data ="""---
apiVersion: v1
kind: Deployment

    """
    return data

@pytest.fixture
def yml_with_no_kind():
    """Return some yml that doesn't have any "kind"
    """
    data ="""---
apiVersion: v1
metadata:
   name: Bear
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
    yaml_parser.read_yaml(empty_data)


def test_get_deployments_no_deployment(simple_yml_data):
    """Test that don't get anything if we don't have any deployments to get
    """
    data = yaml_parser.read_yaml(simple_yml_data)
    deployments = yaml_parser.get_deployments(data)

    assert not deployments

def test_get_deployments(yml_with_deployments):
    """Test that we get two boxes for our two deployments
    """
    data = yaml_parser.read_yaml(yml_with_deployments)
    deployments = yaml_parser.get_deployments(data)

    assert len(deployments) == 2


def test_get_deployments_no_kind(yml_with_no_kind):
    """Test we get no exceptions (but also no deployments) if we don't
    have any "kind" in our yml
    """
    data = yaml_parser.read_yaml(yml_with_no_kind)
    deployments = yaml_parser.get_deployments(data)

    assert not deployments
    
def test_get_no_metadata(yml_with_no_metadata):
    """Test that we get no exceptions if we have no "MetaData" in our yml
    """
    data = yaml_parser.read_yaml(yml_with_no_metadata)
    deployments = yaml_parser.get_deployments(data)

    assert not deployments