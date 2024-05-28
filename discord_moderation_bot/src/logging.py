# logging.py (Python)

import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

# Function to log moderation actions
def log_moderation_action(action, user_id, moderator_id):
    logger.info(f'{action} action performed on user {user_id} by moderator {moderator_id}')