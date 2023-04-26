import json
import sys
from typing import Any, Dict

from geomapper.mapping import create_azure_mapping
from geomapper.utils import get_azure_geocodes_data, get_azure_regions_data


def create_bicep_module(azure_mapping: Dict[str, Dict[str, Any]]) -> str:
    """
    Creates the content for a Bicep module that provides the regional display name,
    display name, and geocode for a given Azure location.

    Args:
        azure_mapping: A dictionary with the Azure mapping data.

    Returns:
        A string with the content for the Bicep module.
    """
    allowed = "[" + "\n  ".join([f"'{key}'" for key in azure_mapping]) + "\n]"
    geomap = json.dumps(azure_mapping, indent=2).replace('"', "'").replace(',', '')
    content = (
        f"@allowed({allowed})\n"
        + "param location string\n"
        + "\n"
        + f"var geomap = {geomap}\n"
        + "\n"
        + "output regionalDisplayName object = geomap[location].regionalDisplayName\n"
        + "output displayName object = geomap[location].displayName\n"
        + "output geoCode object = geomap[location].geoCode\n"
    )
    return content


def main(data_dir: str = "data", modules_dir: str = "modules"):
    """
    Main function that creates the Azure mapping and writes it to a JSON file.

    Args:
        data_dir:    The directory containing the data files. Defaults to 'data' in the
                     root of the project.
        modules_dir: The directory containing the module files. Defaults to 'module' in
                     the root of the project.
    """
    regions_data = get_azure_regions_data(data_dir)
    geocodes_data = get_azure_geocodes_data(data_dir)

    geocode_mapping = create_azure_mapping(
        regions_data=regions_data, geocodes_data=geocodes_data
    )

    bicep_content = create_bicep_module(azure_mapping=geocode_mapping)

    with open(f"{modules_dir}/locations.bicep", "w") as f:
        f.write(bicep_content)


def init():
    """
    Entry point of the program. Calls the main() function.
    """
    if __name__ == "__main__":
        sys.exit(main())


init()
