# Script to authenticate as GitHub App

import dotenv
import github
import os

dotenv.load_dotenv(verbose=True)
GITHUB_PRIVATE_KEY = os.getenv("GITHUB_PRIVATE_KEY")
GITHUB_APP_IDENTIFIER = os.getenv("GITHUB_APP_IDENTIFIER")
GITHUB_WEBHOOK_SECRET = os.getenv("GITHUB_WEBHOOK_SECRET")
