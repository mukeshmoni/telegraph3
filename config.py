"""
Configuration module for the bot status checker.

This module loads environment variables required for the bot to function,
such as bot token, API ID and API HASH.
It also sets up the necessary configuration settings.
"""

from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = int(getenv("API_ID", "28338127"))
    API_HASH = getenv("API_HASH", "c4cb64de16a18f8685a31716a0e2480e")
    BOT_TOKEN = getenv("BOT_TOKEN", "8160540534:AAF8mZO0c9xkBYKsHRQavE2ap9eq8G3x-ug")
    
