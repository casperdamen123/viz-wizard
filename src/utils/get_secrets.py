from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

def get_gcp_secrets(key_vault_uri: str) -> dict:

    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=key_vault_uri, credential=credential)

    gcp_service_account_creds = {
        "type": "service_account",
        "project_id": "viz-wizard",
        "private_key_id": client.get_secret(name='gcpprivatekeyid').value,
        "private_key": client.get_secret(name='gcpprivatekey').value,
        "client_email": "viz-wizard@viz-wizard.iam.gserviceaccount.com",
        "client_id": client.get_secret(name='gcpclientid').value,
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/viz-wizard%40viz-wizard.iam.gserviceaccount.com"
    }

    return gcp_service_account_creds
