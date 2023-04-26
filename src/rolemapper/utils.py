import json
import os
from typing import Any, Dict, List


def get_azure_role_definition_data(data_dir: str = "data") -> List[Dict[str, Any]]:
    """
    Reads the contents of the 'azure-role_definition.json' file in the specified
    directory, and returns its contents as a dictionary.

    Args:
        data_dir: The directory containing the 'azure-role_definition.json' file.
                  Defaults to 'data' in the root of the project.

    Returns:
        A dictionary containing the data from the 'azure-role_definition.json' file.
    """
    project_root = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )

    data_path = os.path.join(project_root, data_dir, "azure-role_definitions.json")

    with open(data_path, "r") as f:
        return json.load(f)
