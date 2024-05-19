# blum.py
import requests
from utils.core.loger.py import logger

BASE_URL = "https://game-domain.blum.codes/api/v1/farming"
USER_CHECK_URL = "https://gateway.blum.codes/v1/user/me"
AUTH_URL = "https://gateway.blum.codes/v1/auth/provider/PROVIDER_TELEGRAM_MINI_APP"

def authenticate():
    # Your authentication logic here
    logger.info('Authenticated successfully')

def get_user_data():
    response = requests.get(USER_CHECK_URL)
    if response.status_code == 200:
        data = response.json()
        username = data['username']
        balance = data['balance']
        return username, balance
    else:
        logger.error('Failed to fetch user data')
        return None, None

def claim_rewards():
    response = requests.post(f"{BASE_URL}/claim")
    if response.status_code == 200:
        logger.info('Claim successful')
        return True
    else:
        logger.error('Claim failed')
        return False

def start_farming():
    response = requests.post(f"{BASE_URL}/start")
    if response.status_code == 200:
        logger.info('Start farming successful')
        return True
    else:
        logger.error('Start farming failed')
        return False
