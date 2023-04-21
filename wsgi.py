import os

os.environ['SECRET_TOKEN'] = 'replace_with_secret_token'

from app import app

if __name__ == "__main__":
    app.run()
