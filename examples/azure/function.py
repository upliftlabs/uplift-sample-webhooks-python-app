import os
import hmac
import hashlib
import logging
logging.basicConfig(level=logging.DEBUG)

import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

def verify_signature(secret, signature, payload):
    # Create a new HMAC instance using the secret
    mac = hmac.new(secret.encode('utf-8'), msg=payload, digestmod=hashlib.sha256)

    # Get the computed signature
    computed_signature = f'sha256={mac.hexdigest()}'
    logging.info (computed_signature)

    # Compare the computed signature with the given signature
    return hmac.compare_digest(computed_signature, signature)


def get_secret_from_vault():
    logging.info('get_secret_from_vault()')

    # Authenticate with Azure AD
    credential = DefaultAzureCredential()
    
    # Retrieve the secret from the Key Vault
    key_vault_url = "https://kvuplift.vault.azure.net/"
    secret_name = 'uplift-secret-token'
    secret_client = SecretClient(vault_url=key_vault_url, credential=credential)
    secret_value = secret_client.get_secret(secret_name).value

    return secret_value


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('HTTP trigger function received a request')

    # Get the Uplift secret key from your app settings
    # secret = os.environ.get('UPLIFT_SECRET')
    secret = get_secret_from_vault()
    logging.info(secret)

    # Get the signature from the request headers
    signature = req.headers.get('x-uplift-signature-256')
    logging.info (signature)

    # Get the payload from the request body
    payload = req.get_body()

    # Verify the signature using the Github secret key
    if not verify_signature(secret, signature, payload):
        return func.HttpResponse(
            'Invalid signature',
            status_code=401
        )

    # Print the payload
    logging.info(payload)

    return func.HttpResponse('Payload printed successfully')