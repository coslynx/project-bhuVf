# config.py (Python)

import os

# Define the configuration class
class Config:
    # Discord API token
    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
    
    # Machine learning model path
    ML_MODEL_PATH = 'models/machine_learning.pkl'
    
    # Third-party API key
    THIRD_PARTY_API_KEY = os.getenv('THIRD_PARTY_API_KEY')
    
    # Database connection details
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = 'password'
    DB_NAME = 'discord_bot_db'