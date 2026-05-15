from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    GITHUB_API_URL = os.getenv(
        "GITHUB_API_URL",
        "https://api.github.com"
    )


settings = Settings()
