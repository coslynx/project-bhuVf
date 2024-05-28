# config_example.py

import os

# Discord Bot Configuration
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = '!'
MODERATION_ROLES = ['Admin', 'Moderator']
WELCOME_CHANNEL = 'welcome'
LOG_CHANNEL = 'mod-logs'
ANNOUNCEMENT_CHANNEL = 'announcements'

# Machine Learning Configuration
ML_MODEL_PATH = 'models/machine_learning_model.pkl'

# Reporting System Configuration
REPORT_CHANNEL = 'reports'

# Third-Party Integration Configuration
THIRD_PARTY_API_KEY = os.getenv('THIRD_PARTY_API_KEY')

# User Reputation System Configuration
REPUTATION_THRESHOLD = 5

# Data Visualization Configuration
DATA_VISUALIZATION_THEME = 'dark'

# Documentation Configuration
DOCUMENTATION_URL = 'https://yourdocumentation.com'

# Security Audit Configuration
SECURITY_AUDIT_INTERVAL = 30  # in days
SECURITY_AUDIT_CHANNEL = 'security-audit'