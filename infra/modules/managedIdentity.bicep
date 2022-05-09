targetScope = 'resourceGroup'

param userManagedIdentityName string = 'viz-wizard'
param location string = resourceGroup().location

@description('The built-in roles to assign to the managed identity')
var roles = [
  '7f951dda-4ed3-4680-a7ca-43fe172d538d' // https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#acrpull 
  '8311e382-0749-4cb8-b61a-304f252e45ec' // https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#acrpush 
  '9b7fa17d-e63e-47b0-bb0a-15c516ac86ec' // https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles##sql-db-contributor 
  '00482a5a-887f-4fb3-b363-3b7fe8e74483' // https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#key-vault-administrator
]

@description('Create managed identity')
resource managedIdentity 'Microsoft.ManagedIdentity/userAssignedIdentities@2018-11-30' = {
  name: userManagedIdentityName
  location: location
}

@description('Define needed built-in roles')
resource roleDefinitions 'Microsoft.Authorization/roleDefinitions@2018-01-01-preview' existing = [for role in roles: {
  name: role
}]

@description('Assign roles to managed identity')
resource roleAssignments 'Microsoft.Authorization/roleAssignments@2020-10-01-preview' =  [for (role, i) in roles: {
  name: guid(resourceGroup().id, managedIdentity.id, role)
  properties: {
    roleDefinitionId: roleDefinitions[i].id
    principalId: managedIdentity.properties.principalId
    principalType: 'ServicePrincipal'
  }
}]

output userManagedIdentityPrincipalId string = managedIdentity.properties.principalId
output userManagedIdentityClientId string = managedIdentity.properties.clientId
output userManagedIdentityId string = managedIdentity.id
