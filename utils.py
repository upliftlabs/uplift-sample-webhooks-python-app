import json
import hmac
import hashlib
import logging
logging.basicConfig(level=logging.DEBUG)


def create_signature(secret, payload):
    """
    Computes the HMAC signature for a JSON payload using a secret key.
    
    Args:
        secret (str): The secret key used to compute the HMAC signature.
        payload (dict): The JSON payload for which to compute the signature.
    
    Returns:
        str: The computed signature with a 'sha256=' prefix.
    
    Example:
        secret_key = 'your_secret_key'
        payload = {"key": "value"}
        signature = create_signature(secret_key, payload)
    """

    # Convert the payload to a JSON string
    payload_str = json.dumps(payload)

    # Encode the payload string and secret as UTF-8
    payload_bytes = payload_str.encode('utf-8')
    secret_bytes = secret.encode('utf-8')

    # Compute the HMAC signature
    mac = hmac.new(secret_bytes, msg=payload_bytes, digestmod=hashlib.sha256)
    signature = f'sha256={mac.hexdigest()}'
    logging.info (signature)   

    return signature


def verify_signature(secret, signature, payload):
    """
    Verifies the integrity of a payload using an HMAC-based signature.
    
    Args:
        secret (str): The secret key used to compute the HMAC signature.
        signature (str): The HMAC signature to verify.
        payload (bytes): The payload for which to verify the signature.
    
    Returns:
        bool: True if the given signature matches the computed signature, False otherwise.
    
    Example:
        secret_key = 'your_secret_key'
        received_signature = 'sha256=example_signature'
        payload = b'{"key": "value"}'
        is_valid = verify_signature(secret_key, received_signature, payload)
    """
    
    # Create a new HMAC instance using the secret
    mac = hmac.new(secret.encode('utf-8'), msg=payload, digestmod=hashlib.sha256)

    # Get the computed signature
    computed_signature = f'sha256={mac.hexdigest()}'
    logging.info (computed_signature)

    # Compare the computed signature with the given signature
    return hmac.compare_digest(computed_signature, signature)