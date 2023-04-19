import json
from typing import Dict, Any

from geomapper.utils import get_azure_geocodes_data, get_azure_regions_data


def create_azure_mapping() -> Dict[str, Any]:
    """
    Creates a mapping of Azure regions to their respective geocodes, by combining
    data from 'azure-regions.json' and 'azure-geocodes.xml' files.

    Returns:
        A dictionary containing the Azure region to geocode mapping.
    """
    regions_data = get_azure_regions_data()
    geocodes_data = get_azure_geocodes_data()
    mapping = {}

    for region in regions_data:
        display_name = region["displayName"]
        if display_name in geocodes_data:
            mapping[region["name"]] = {
                "name": region["name"],
                "regionalDisplayName": region["regionalDisplayName"],
                "geoCode": geocodes_data[display_name],
            }

    return mapping


if __name__ == "__main__":
    geocode_mapping = create_azure_mapping()
    geocode_json = json.dumps(geocode_mapping, indent=4)

    with open("data/geo.mapping.json", "w") as f:
        f.write(geocode_json)
