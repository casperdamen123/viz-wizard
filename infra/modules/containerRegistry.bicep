targetScope = 'resourceGroup'

param environmentType string
param location string = resourceGroup().location
param userManagedIdentityId string 
param webAppName string = 'web-app-viz-wizard'
var acrSku = (environmentType == 'prod') ? 'Standard' : 'Basic'

@description('Name of the container registry')
var acrName = 'acrvizwizard'

@description('Name of the webhook that updates the web app when an updated new Docker image is pushed')
var webHookName = 'vizwizwebhook' 

@description('Base of the webhook URL that is needed to update web app when new Docker image is pushed')
var webAppScmUri  = list(publishingCredentialsWebApp.id, publishingCredentialsWebApp.apiVersion).properties.scmUri

resource acrResource 'Microsoft.ContainerRegistry/registries@2021-09-01' = {
  name: acrName
  location: location
  sku: {
    name: acrSku
  }
  identity: {
    type: 'UserAssigned'
    userAssignedIdentities: {
      '${userManagedIdentityId}' : {}
    }
  }
}

resource publishingCredentialsWebApp 'Microsoft.Web/sites/config@2021-03-01' existing = {
  name: '${webAppName}/publishingcredentials'
}

@description('Web hook to update Docker image for web app after new image is pushed to container registry')
resource dockerWebHook 'Microsoft.ContainerRegistry/registries/webhooks@2020-11-01-preview' = {
  parent: acrResource
  location: location
  name: webHookName
  properties: {
    serviceUri: '${webAppScmUri}/docker/hook'
    status: 'enabled'
    actions: [
      'push'
    ]
  }
}

output containerRegistryloginServer string = acrResource.properties.loginServer
output containerRegistryName string = acrResource.name
