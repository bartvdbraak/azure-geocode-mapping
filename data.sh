#!/bin/bash

# Declare constants
readonly BASEDIR="$(cd "$(dirname "$0")" && pwd)"
readonly REGIONS_OUTPUT_FILE="$BASEDIR/data/azure-regions.json"
readonly GEOCODES_OUTPUT_FILE="$BASEDIR/data/azure-geocodes.xml"
readonly GEOCODES_SOURCE_URL="https://raw.githubusercontent.com/MicrosoftDocs/azure-docs/main/articles/backup/scripts/geo-code-list.md"
readonly ROLE_DEFINITIONS_OUTPUT_FILE="$BASEDIR/data/azure-role_definitions.json"

# Check if Azure CLI is installed
check_azure_cli() {
  if ! command -v az &> /dev/null; then
    printf "Error: Azure CLI is not installed.\n" >&2
    exit 1
  fi
}

# Check if there is an active account
check_active_account() {
  if ! az account show &> /dev/null; then
    printf "Error: No active Azure account found.\n" >&2
    exit 1
  fi
}

# Get azure regions and save to azure-regions.json
get_azure_regions() {
  az account list-locations \
    --query "[?metadata.regionType=='Physical'] .{name:name,displayName:displayName,regionalDisplayName:regionalDisplayName}" \
    --output json > "$REGIONS_OUTPUT_FILE"
}

# Get azure geocodes and save to azure-geocodes.xml
get_azure_geocodes() {
  source_content=$(curl -s "$GEOCODES_SOURCE_URL")
  if [[ $source_content =~ .*\<GeoCodeList\>(.*)\<\/GeoCodeList\>.* ]]; then
    filtered_content="<GeoCodeList>${BASH_REMATCH[1]}</GeoCodeList>"
  else
    printf "Error: Failed to extract GeoCodeList from source content.\n" >&2
    exit 1
  fi
  printf "%s" "$filtered_content" > "$GEOCODES_OUTPUT_FILE"
}

# Get azure regions and save to azure-regions.json
get_azure_role_definitions() {
  az role definition list > "$ROLE_DEFINITIONS_OUTPUT_FILE"
}

# Main function
main() {
  check_azure_cli
  check_active_account
  get_azure_regions
  get_azure_geocodes
  get_azure_role_definitions
}

# Call the main function
main
