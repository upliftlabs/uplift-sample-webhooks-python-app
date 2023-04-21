import os
import json
import requests
from multiprocessing import Process
from app import app

def run_app():
    app.run()

def test_webhook():
    url = 'http://localhost:5000/webhook'

    headers = {
        'Content-Type': 'application/json',
        'x-uplift-signature-256': 'example_signature'
    }

    data = {
        'key': 'value'
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    assert response.status_code == 200

if __name__ == '__main__':
    # Set the SECRET_TOKEN environment variable for testing
    os.environ['SECRET_TOKEN'] = 'test_secret_token'

    # Run the Flask app in a separate process
    process = Process(target=run_app)
    process.start()

    # Run the test
    test_webhook()

    # Terminate the Flask app process
    process.terminate()
