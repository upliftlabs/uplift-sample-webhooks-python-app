import os

os.environ['SECRET_TOKEN'] = 'your_secret_token_here'

from app import app

if __name__ == "__main__":
    app.run()
