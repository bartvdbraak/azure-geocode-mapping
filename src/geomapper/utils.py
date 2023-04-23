import json
import os
import xml.etree.ElementTree as ET
from typing import Any, Dict, List


def get_azure_regions_data(data_dir: str = "data") -> List[Dict[str, Any]]:
    """
    Reads the contents of the 'azure-regions.json' file in the specified directory,
    and returns its contents as a dictionary.

    Args:
        data_dir: The directory containing the 'azure-regions.json' file. Defaults to
                  'data' in the root of the project.

    Returns:
        A dictionary containing the data from the 'azure-regions.json' file.
    """
    project_root = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )

    data_path = os.path.join(project_root, data_dir, "azure-regions.json")

    with open(data_path, "r") as f:
        return json.load(f)


def get_azure_geocodes_data(data_dir: str = "data") -> Dict[str, Any]:
    """
    Reads the contents of the 'azure-geocodes.xml' file in the specified directory,
    and returns its contents as a dictionary.

    Args:
        data_dir: The directory containing the 'azure-geocodes.xml' file. Defaults to
                  'data' in the root of the project.

    Returns:
        A dictionary containing the data from the 'azure-geocodes.xml' file.
    """
    project_root = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )

    data_path = os.path.join(project_root, data_dir, "azure-geocodes.xml")

    tree = ET.parse(data_path)
    root = tree.getroot()
    return {child.attrib["RegionName"]: child.attrib["GeoCode"] for child in root}
