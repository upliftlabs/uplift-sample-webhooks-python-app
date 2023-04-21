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
