"""
config.py
Loads configuration values from the .env file.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# OpenAI Configuration

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# News API Configuration

NEWS_API_KEY = os.getenv("NEWS_API_KEY")


# Email Configuration

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


# SMTP Configuration

SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))


# Recipient

RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")



# Validation Function

def validate_config():
    """
    Checks whether all required environment variables exist.
    """

    required = {
        "OPENAI_API_KEY": OPENAI_API_KEY,
        "NEWS_API_KEY": NEWS_API_KEY,
        "EMAIL_ADDRESS": EMAIL_ADDRESS,
        "EMAIL_PASSWORD": EMAIL_PASSWORD,
        "RECIPIENT_EMAIL": RECIPIENT_EMAIL,
    }

    missing = []

    for key, value in required.items():
        if not value:
            missing.append(key)

    if missing:
        raise ValueError(
            f"Missing environment variables: {', '.join(missing)}"
        )
