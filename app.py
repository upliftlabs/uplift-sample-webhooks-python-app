import os
from flask import Flask, request
import json
import os
from utils import verify_signature
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/webhook/submit', methods=['POST'])
def webhook_submit():
    """
    Handles incoming webhook requests by verifying the signature and logging the payload.
    
    This Flask route listens for POST requests at the '/webhook/submit' path. It retrieves
    the Uplift secret key from the environment, the 'x-uplift-signature-256' header from
    the incoming request, and the request payload as bytes. The route verifies the signature
    using the provided secret key and returns an HTTP 401 response if the signature is invalid.
    If the signature is valid, the route logs the payload and returns an HTTP 200 response.
    
    Returns:
        Tuple[str, int]: A tuple containing a response message and an HTTP status code.
    """

    logging.info('webhook function received a request')

    # Get the Uplift secret key from your app settings
    secret_token = os.environ.get('SECRET_TOKEN')
    logging.info(secret_token)

    # Get the signature from the request headers
    signature = request.headers.get('x-uplift-signature-256')
    logging.info (signature)

    # Get the payload from the request body as bytes
    payload = request.get_data()

    # Verify the signature using the Uplift secret key
    if not verify_signature(secret_token, signature, payload):
        return 'Invalid signature', 401

    # Print the payload
    logging.info(payload)
    return 'Payload printed successfully', 200

if __name__ == '__main__':
    app.run()
