#!/bin/bash

# Declare constants
readonly BASEDIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
readonly MODULES_FOLDER="$BASEDIR/modules"
readonly REGISTRY_ENDPOINT="bartvdbraak.azurecr.io"

# Check if Azure CLI is installed
check_azure_cli() {
  if ! command -v az > /dev/null; then
    echo "Error: Azure CLI is not installed." >&2
    exit 1
  fi
}

# Check if there is an active account
check_active_account() {
  if ! az account show > /dev/null; then
    echo "Error: No active Azure account found." >&2
    exit 1
  fi
}

# Publish modules
publish_modules() {
  for module_path in "$MODULES_FOLDER"/*.bicep; do
    module_name=$(basename "$module_path" .bicep)
    az bicep publish \
      --file "$module_path" \
      --target "br:$REGISTRY_ENDPOINT/bicep/modules/$module_name:v1" #\
      # --documentation-uri "https://www.contoso.com/exampleregistry.html"
  done
}

# Main function
main() {
  check_azure_cli
  check_active_account
  publish_modules
}

main "$@"
