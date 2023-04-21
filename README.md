# Python Webhook Application

This repository contains a simple Python webhook application using Flask and gunicorn. The application consumes a webhook, prints the body contents, a header attribute called `x-uplift-signature-256`, and an environment variable called `SECRET_TOKEN` to the terminal.

## Files

- `app.py`: Contains the Flask application that defines the webhook route.
- `wsgi.py`: Contains the WSGI configuration and sets the `SECRET_TOKEN` environment variable.
- `utils.py`: Utility functions for creating and verifying a HMAC signature for a JSON payload using a secret key.
- `test.py`: A test script to run the webhook application locally and send a test request.
- `requirements.txt`: A list of required Python packages for the application.
- `.gitignore`: A list of files and directories that should be ignored by Git.

## Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

## Setup

1. Clone the repository to your local machine.

```bash
git clone https://github.com/yourusername/uplift-sample-webhooks-python-app.git
```

2. Navigate to the project directory.

```bash
cd uplift-sample-webhooks-python-app
```
3. Create a virtual environment (optional, but recommended).

```bash
python -m venv venv
```

4. Activate the virtual environment.

* On Linux or macOS:

```bash
source venv/bin/activate
```

* On Windows

```bash
venv\Scripts\activate
```

5. Install the required Python packages.

```bash
pip install -r requirements.txt

```

## Running the Application Locally

1. Set the `SECRET_TOKEN` environment variable in the `wsgi.py` file.

```bash
os.environ['SECRET_TOKEN'] = 'replace_with_secret_token'
```

Replace `'replace_with_secret_token'` with your actual secret token value. 

2. Start the Flask development server.
```bash
python app.py
```

The application will be running on http://localhost:5000.

## Testing the Application

1. Open a new terminal window or tab, and make sure you're in the project directory.
2. Run the test script.

```bash
python test.py
```

The test script will start the Flask app, send a POST request to the `/webhook/submit` endpoint with a JSON payload and the `x-uplift-signature-256` header, and then print the webhook body, header value, and environment variable to the terminal.

If the test is successful, the script will exit without any errors.

## Deploying Flask Application on GoDaddy cPanel

1. **Log in to your GoDaddy cPanel account**: Access your GoDaddy account and navigate to the cPanel dashboard.

2. **Create a Python application environment**: In the cPanel dashboard, look for the "Software" section and click on "Setup Python App". Choose the Python version you want to use, and then set the application root and the application URL. Click on "Create" to create the Python application environment.

3. **Upload your application files**: You can use an FTP client (like FileZilla) or the cPanel File Manager to upload your application files to the server. Make sure to upload the files to the application root directory you specified in step 2.

4. **Install the required packages**: In your cPanel Python application environment, you'll see a "Packages" section. Click on "Enter" and then input the package names and their respective versions (one at a time) that your application requires (e.g., Flask, gunicorn, requests). Click on "Install" to install each package.

5. **Configure your application**: In the cPanel Python application environment, you'll see a section called "App Configuration". Here, you should specify the entry point to your application. Set the "WSGI" field to the path of your WSGI file (e.g., `app:app` if your main file is named `app.py`).

6. **Set environment variables**: In the "Environment Variables" section of the cPanel Python application environment, add any necessary environment variables (such as `SECRET_TOKEN`).

7. **Restart your application**: In the cPanel Python application environment, click on "Restart" to apply the changes and start your application.

8. **Test your application**: Access your application using the application URL you set in step 2. Check if the webhook functionality is working as expected.

Please note that specific steps may vary slightly depending on your cPanel version and configuration. If you encounter any issues or need further assistance, you can consult GoDaddy's help documentation or contact their support team.
