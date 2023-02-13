import os


# for AAD
CLIENT_ID = os.environ['AAD_CLIENT_ID']
CLIENT_SECRET = os.environ['AAD_CLIENT_SECRET']
AUTHORITY = f"https://login.microsoftonline.com/{os.environ['AAD_TENANT_ID']}"
BASE_REDIRECT_PATH = "/api/auth/login_callback"
REDIRECT_PATH = f"https://localhost:3001{BASE_REDIRECT_PATH}"
SCOPE = ['user.read']


# for flask session
SESSION_PERMANENT = False
SESSION_TYPE = "filesystem"
