from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# GitHub token
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
