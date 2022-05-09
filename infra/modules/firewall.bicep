/*
We use a separate template here to avoid a circular error between the app and sqlServer module. The outbound IP addresses of the app should be used in the 
SQL server firewall setup, while the SQL server details such as server hostname are stored as environment variables in the web app so the source code 
can leverage these values. 
*/

param sqlServerFirewallRules string = 'viz-wizard-firewall'
param sqlServerName string = 'viz-wizard'
param webAppOutboundIpAddresses string 

@description('List with all web app outbound IP addresses that should be added to the firewall settings')
var webAppOutboundIpAddressesList = split(webAppOutboundIpAddresses, ',')

resource sqlServer 'Microsoft.Sql/servers@2020-11-01-preview' existing = {
  name: sqlServerName
}

resource fireWallRules 'Microsoft.Sql/servers/firewallRules@2021-11-01-preview' = [for ip in webAppOutboundIpAddressesList:  {
  parent: sqlServer
  name: '${sqlServerFirewallRules}_${ip}'
  properties: {
    startIpAddress: ip
    endIpAddress: ip
  }
}]
