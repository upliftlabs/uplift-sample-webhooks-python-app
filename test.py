import os
import json
import requests
from multiprocessing import Process
from app import app
from utils import create_signature, verify_signature

# Test Payload
data = {
    'key': 'value'
}

def run_app():
    app.run()

def test_webhook(secret):
    url = 'http://localhost:5000/webhook/submit'

    headers = {
        'Content-Type': 'application/json',
        'x-uplift-signature-256': create_signature(secret, data)
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    assert response.status_code == 200


if __name__ == '__main__':
    # Set the SECRET_TOKEN environment variable for testing
    os.environ['SECRET_TOKEN'] = 'replace_with_secret_token'

    # Run the Flask app in a separate process
    process = Process(target=run_app)
    process.start()

    # Run the test
    test_webhook('replace_with_secret_token')

    # Terminate the Flask app process
    process.terminate()

    # sig = create_signature('secret_token', data)
    # print(verify_signature('secret_token', sig, json.dumps(data).encode('utf-8')))
