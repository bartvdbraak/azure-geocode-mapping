import json
import sys
import textwrap
from typing import List

from rolemapper.utils import get_azure_role_definition_data


def create_bicep_module(role_definitions: List[dict]) -> str:
    allowed_roles = [rd["roleName"] for rd in role_definitions]
    allowed = "[" + "\n  ".join([f"'{role}'" for role in allowed_roles]) + "\n]"
    role_map = {}
    for rd in role_definitions:
        role_map[rd["roleName"]] = {"id": rd["name"]}
    role_map = json.dumps(role_map, indent=2).replace('"', "'").replace(',', '')
    content = textwrap.dedent(
        f"@allowed({allowed})\n"
        + "param roleName string\n"
        + "\n"
        + f"var roleMap = {role_map}\n"
        + "\n"
        + "output id string = roleMap[roleName].id\n"
    )
    return content


def main(data_dir: str = "data", modules_dir: str = "modules"):
    """
    Main function that creates the Bicep module content and writes it to a file.

    Args:
        data_dir:    The directory containing the data files. Defaults to 'data' in the
                     root of the project.
        modules_dir: The directory containing the module files. Defaults to 'module' in
                     the root of the project.
    """
    role_definition_data = get_azure_role_definition_data(data_dir)

    bicep_content = create_bicep_module(role_definitions=role_definition_data)

    with open(f"{modules_dir}/role_definition_ids.bicep", "w") as f:
        f.write(bicep_content)


def init():
    """
    Entry point of the program. Calls the main() function.
    """
    if __name__ == "__main__":
        sys.exit(main())


init()
