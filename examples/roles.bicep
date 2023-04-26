
module roles 'br:bartvdbraak.azurecr.io/bicep/modules/role_definition_ids:v1' = {
  name: 'myRole'
  params: {
    roleName: 'AcrPull'
  }
}

var roleId = resourceId('Microsoft.Authorization/roleAssignments', roles.outputs.id)

resource roleAssignment 'Microsoft.Authorization/roleAssignments@2020-10-01-preview' = {
  name: guid(resourceGroup().id, 'principalId', roles.outputs.id)
  properties: {
    roleDefinitionId: roleId
    principalId: 'principalId'
    principalType: 'principalType'
  }
}
