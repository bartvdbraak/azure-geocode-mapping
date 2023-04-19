import json
import os

import pytest

from geomapper.mapping import create_azure_mapping, main


@pytest.fixture(scope="module")
def azure_mapping_data():
    return {
        "eastus": {
            "displayName": "East US",
            "regionalDisplayName": "(US) East US",
            "geoCode": "eus",
        },
        "eastus2": {
            "displayName": "East US 2",
            "regionalDisplayName": "(US) East US 2",
            "geoCode": "eus2",
        },
        "southcentralus": {
            "displayName": "South Central US",
            "regionalDisplayName": "(US) South Central US",
            "geoCode": "scus",
        },
    }


def test_create_azure_mapping(azure_mapping_data):
    expected_mapping = azure_mapping_data
    assert create_azure_mapping(data_dir='tests/data') == expected_mapping


def test_main(azure_mapping_data):
    expected_mapping = azure_mapping_data
    main()

    with open(os.path.join('tests/data', "geo.mapping.json"), "r") as f:
        assert json.load(f) == expected_mapping