import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


def get_secret(key_vault_uri: str, key_name: str) -> str:
    """Get secret for Azure Key Vault
    Args:
        key_vault_uri (str): URI of Azure key vault
    Returns:
        key_name (str): Name of the secret to retrieve
    """
    credential = DefaultAzureCredential(managed_identity_client_id=os.getenv('USER_MANAGED_IDENTITY_CLIENT_ID'))
    client = SecretClient(vault_url=key_vault_uri, credential=credential)

    return client.get_secret(name=key_name).value
    