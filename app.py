import os
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    content = request.get_json()
    uplift_signature = request.headers.get('x-uplift-signature-256')
    secret_token = os.environ.get('SECRET_TOKEN')

    print("Webhook Body:")
    print(json.dumps(content, indent=4))

    print("\nHeader - x-uplift-signature-256:")
    print(uplift_signature)

    print("\nEnvironment Variable - secret-token:")
    print(secret_token)

    return 'OK', 200

if __name__ == '__main__':
    app.run()
