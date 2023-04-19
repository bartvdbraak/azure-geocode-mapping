import pytest

from geomapper.utils import get_azure_regions_data, get_azure_geocodes_data


@pytest.fixture(scope="module")
def regions_data():
    return [
        {
            "displayName": "East US",
            "name": "eastus",
            "regionalDisplayName": "(US) East US"
        },
        {
            "displayName": "East US 2",
            "name": "eastus2",
            "regionalDisplayName": "(US) East US 2"
        },
        {
            "displayName": "South Central US",
            "name": "southcentralus",
            "regionalDisplayName": "(US) South Central US"
        }
    ]


@pytest.fixture(scope="module")
def geocodes_data():
    return {
        "East US": "eus",
        "East US 2": "eus2",
        "South Central US": "scus",
    }


def test_get_azure_regions_data(regions_data):
    assert get_azure_regions_data(data_dir='tests/data') == regions_data


def test_get_azure_geocodes_data(geocodes_data):
    assert get_azure_geocodes_data(data_dir='tests/data') == geocodes_data
