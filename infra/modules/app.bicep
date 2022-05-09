param location string = resourceGroup().location

@description('Name of container registry that contains Docker image')
param acrName string 

@description('Provide Docker image and tag name to run on web app')
param dockerImageAndTag string = 'app:latest'

@description('Name of web app to deploy')
param webAppName string = 'web-app-viz-wizard'

@description('Indicates whether the Docker image is already pushed to the container registry')
param dockerImagePushed bool

param environmentType string
param userManagedIdentityId string
param userManagedIdentityClientId string

// Needed parameters to set environment variables in web app, which are leveraged by the app source code 
param sqlServerLoginName string
param sqlServerHostName string 
param sqlServerName string
param sqlDatabaseName string
param keyVaultUri string

@description('App plan skus depending on environment type')
var appPlanSkuName = (environmentType == 'prod') ? 'S1' : 'B1'
var appPlanSkuTier = (environmentType == 'prod') ? 'Standard' : 'Basic'

var farmName = '${webAppName}-farm'

resource farm 'Microsoft.Web/serverfarms@2021-03-01' = {
  name: farmName
  location: location
  sku: {
    name: appPlanSkuName
    tier: appPlanSkuTier
  }
  kind: 'linux'
  properties: {
    targetWorkerSizeId: 0
    targetWorkerCount: 1
    reserved: true
  }
}

resource webApp 'Microsoft.Web/sites@2021-03-01' = {
  name: webAppName
  location: location
  identity: {
    type: 'UserAssigned'
    userAssignedIdentities: {
      '${userManagedIdentityId}' : {}
    }
  }
  properties: {
    siteConfig: {
      acrUseManagedIdentityCreds: true
      acrUserManagedIdentityID: userManagedIdentityClientId
      detailedErrorLoggingEnabled: true
      appSettings: [
        {
          name: 'DOCKER_REGISTRY_SERVER_URL'
          value: 'https://${acrName}.azurecr.io'
        }
        {
          name: 'DOCKER_ENABLE_CI'
          value: 'true'
        }
        {
          name: 'WEBSITES_PORT'
          value: '8501'
        }
        {
          name: 'WEBSITES_ENABLE_APP_SERVICE_STORAGE'
          value: 'false'
        }
        {
          name: 'DB_SERVER_HOSTNAME'
          value: sqlServerHostName
        }
        {
          name: 'DB_SERVER_NAME'
          value: sqlServerName
        }
        {
          name: 'DB_NAME'
          value: sqlDatabaseName
        }
        {
          name: 'DB_LOGIN'
          value: sqlServerLoginName
        }
        {
          name: 'KV_URI'
          value: keyVaultUri
        }
        {
          name: 'USER_MANAGED_IDENTITY_CLIENT_ID'
          value: userManagedIdentityClientId
        }
      ]
      linuxFxVersion: dockerImagePushed ? 'DOCKER|${acrName}.azurecr.io/${dockerImageAndTag}' : '' 
    }
    serverFarmId: farm.id
  }
}

output webAppName string = webApp.name
output webAppIps string = webApp.properties.outboundIpAddresses
