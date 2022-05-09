param sqlServerName string = 'viz-wizard'
param sqlDatabaseName string = 'logging'
param location string = resourceGroup().location
param administratorLogin string = 'vizwizard' 
@secure()
param administratorLoginPassword string 
param environmentType string
param userManagedIdentityId string 

var sqlServerSkuName = (environmentType == 'prod') ? 'S1' : 'Basic'
var sqlServerSkuTier = (environmentType == 'prod') ? 'Standard' : 'Basic'

resource sqlServer 'Microsoft.Sql/servers@2020-11-01-preview' = {
  name: sqlServerName
  location: location
  identity: {
    type: 'UserAssigned'
    userAssignedIdentities: {
      '${userManagedIdentityId}' : {}
    }
  }
  properties: {
    administratorLogin: administratorLogin
    administratorLoginPassword: administratorLoginPassword
    primaryUserAssignedIdentityId: userManagedIdentityId
  }
}

resource sqlDataBase 'Microsoft.Sql/servers/databases@2020-11-01-preview' = {
  parent: sqlServer
  name: sqlDatabaseName
  location: location
  sku: {
    name: sqlServerSkuName
    tier: sqlServerSkuTier
  }
}

output sqlServerLoginName string = sqlServer.properties.administratorLogin
output sqlServerName string = sqlServer.name
output sqlServerHostName string = environment().suffixes.sqlServerHostname
output sqlDatabaseName string = sqlDataBase.name
