targetScope = 'resourceGroup'

param location string = resourceGroup().location
param tenantId string = subscription().tenantId

param keyVaultName string = 'viz-wiz'

@description('A unique suffix to add to keyvault name that need to be globally unique')
param resourceSuffix string = uniqueString(resourceGroup().id)

@description('Azure SQL server password to store in key vault')
@secure()
param sqlServerPassword string 

@description('User managed identity that should have access to key vault')
param userManagedIdentityPrincipalId string 

var uniqueKeyVaultName = '${keyVaultName}-${resourceSuffix}'

// Setup Key Vault and provide access to web app
resource keyVault 'Microsoft.KeyVault/vaults@2021-04-01-preview' = {
  name: uniqueKeyVaultName
  location: location
  properties: {
    sku: {
      family: 'A'
      name: 'standard'
    }
    tenantId: tenantId
    enabledForTemplateDeployment: true
    enableRbacAuthorization: true
    accessPolicies: [
      {
      tenantId: tenantId
      objectId: userManagedIdentityPrincipalId
      permissions: {
        secrets: [
          'list'
          'get'
        ]
      }
      }
    ]
  }
}

// Add SQL server key
resource keyVaulSecret 'Microsoft.KeyVault/vaults/secrets@2021-11-01-preview' = {
  parent: keyVault
  name: 'sqlServerPassword'
  properties: {
    value: sqlServerPassword
  }
}

output keyVaultUri string = keyVault.properties.vaultUri
output keyVaultName string = keyVault.name
