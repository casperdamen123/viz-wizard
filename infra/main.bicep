targetScope = 'subscription'

@description('Determine environment to deploy, options are dev for development and prod for production')
@allowed([
  'dev'
  'prod'
])
param environmentType string = 'dev'

param location string = 'eastus'
param resourceGroupName string = 'viz-wizard'
param webAppName string = 'web-app-viz-wizard'

@description('Set password for SQL server')
@secure()
param sqlAdminServerPassword string

@description('Indicate whether the build image is pushed to the container registry, build and push happens in Devops pipeline')
param dockerImagePushed bool 

resource newResourceGroup 'Microsoft.Resources/resourceGroups@2021-04-01' = {
  name: resourceGroupName
  location: location
}

module managedIdentityModule 'modules/managedIdentity.bicep' = {
  name: 'managedIdentity'
  scope: newResourceGroup
  params: {
    location: location
  }
}
module containerRegistryModule 'modules/containerRegistry.bicep' = {
  name: 'containerRegistry'
  scope: newResourceGroup
  params : {
    location: location
    environmentType: environmentType
    userManagedIdentityId: managedIdentityModule.outputs.userManagedIdentityId
    webAppName: webAppName
  }
}

module keyVaultModule 'modules/keyvault.bicep'= {
  name: 'keyVault'
  scope: newResourceGroup
  params: {
    location: location
    sqlServerPassword: sqlAdminServerPassword
    userManagedIdentityPrincipalId: managedIdentityModule.outputs.userManagedIdentityPrincipalId
  }
}

module sqlServerModule 'modules/sqlServer.bicep' = {
  name: 'sqlServer'
  scope: newResourceGroup
  params: {
    location: location
    environmentType: environmentType
    administratorLoginPassword: sqlAdminServerPassword
    userManagedIdentityId: managedIdentityModule.outputs.userManagedIdentityId
  }
}

module appModule 'modules/app.bicep' = {
  name: 'app'
  scope: newResourceGroup
  params: {
    location: location
    webAppName: webAppName
    acrName: containerRegistryModule.outputs.containerRegistryName
    environmentType: environmentType
    dockerImagePushed: dockerImagePushed
    userManagedIdentityId: managedIdentityModule.outputs.userManagedIdentityId
    userManagedIdentityClientId: managedIdentityModule.outputs.userManagedIdentityClientId
    sqlServerHostName: sqlServerModule.outputs.sqlServerHostName
    sqlServerName: sqlServerModule.outputs.sqlServerName
    sqlDatabaseName: sqlServerModule.outputs.sqlDatabaseName
    sqlServerLoginName: sqlServerModule.outputs.sqlServerLoginName
    keyVaultUri: keyVaultModule.outputs.keyVaultUri
  }
}

module fireWallModule 'modules/firewall.bicep' = {
  name: 'firewall'
  scope: newResourceGroup
  params: {
    webAppOutboundIpAddresses: appModule.outputs.webAppIps
  }
}
