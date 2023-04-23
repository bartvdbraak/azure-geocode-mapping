import json
import sys
from typing import Dict, Any

from geomapper.utils import get_azure_geocodes_data, get_azure_regions_data


def create_azure_mapping(data_dir: str = "data") -> Dict[str, Any]:
    """
    Creates a mapping of Azure regions to their respective geocodes, by combining
    data from 'azure-regions.json' and 'azure-geocodes.xml' files.

    Args:
        data_dir: The directory containing the data files. Defaults to 'data' in the
                  root of the project.

    Returns:
        A dictionary containing the Azure region to geocode mapping.
    """
    regions_data = get_azure_regions_data(data_dir)
    geocodes_data = get_azure_geocodes_data(data_dir)
    mapping = {}

    for region in regions_data:
        display_name = region["displayName"]
        if display_name in geocodes_data:
            mapping[region["name"]] = {
                "displayName": display_name,
                "regionalDisplayName": region["regionalDisplayName"],
                "geoCode": geocodes_data[display_name],
            }

    return mapping


def main(data_dir: str = "data"):
    """
    Main function that creates the Azure mapping and writes it to a JSON file.

    Args:
        data_dir: The directory containing the data files. Defaults to 'data' in the
                  root of the project.
    """
    geocode_mapping = create_azure_mapping(data_dir)
    geocode_json = json.dumps(geocode_mapping, indent=4)

    with open(f"{data_dir}/geo.mapping.json", "w") as f:
        f.write(geocode_json)


def init():
    """
    Entry point of the program. Calls the main() function.
    """
    if __name__ == "__main__":
        sys.exit(main())


init()
