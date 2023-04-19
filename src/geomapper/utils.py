import json
import xml.etree.ElementTree as ET
from typing import Dict, Any, List


def get_azure_regions_data() -> List[Dict[str, Any]]:
    """
    Reads the contents of the 'azure-regions.json' file in the 'data' directory,
    and returns its contents as a dictionary.

    Returns:
        A dictionary containing the data from the 'azure-regions.json' file.
    """
    with open("data/azure-regions.json", "r") as f:
        return json.load(f)


def get_azure_geocodes_data() -> Dict[str, Any]:
    """
    Reads the contents of the 'azure-geocodes.xml' file in the 'data' directory,
    and returns its contents as a dictionary.

    Returns:
        A dictionary containing the data from the 'azure-geocodes.xml' file.
    """
    tree = ET.parse("data/azure-geocodes.xml")
    root = tree.getroot()
    return {child.attrib["RegionName"]: child.attrib["GeoCode"] for child in root}
