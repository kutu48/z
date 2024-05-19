import requests
from utils.core.logger import logger

AUTH_URL = "https://gateway.blum.codes/v1/auth/provider/PROVIDER_TELEGRAM_MINI_APP"
BASE_URL = "https://game-domain.blum.codes/api/v1/farming"
USER_CHECK_URL = "https://gateway.blum.codes/v1/user/me"

def authenticate():
    response = requests.post(AUTH_URL, json={})
    if response.status_code == 200:
        logger.info("Authenticated successfully")
        return response.json()['token']
    else:
        logger.error("Authentication failed")
        return None

def get_user_info(token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(USER_CHECK_URL, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        logger.error("Failed to get user info")
        return None

def claim_reward(token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.post(f"{BASE_URL}/claim", headers=headers)
    if response.status_code == 200:
        logger.info("Claim successful")
        return response.json()
    else:
        logger.error("Claim failed")
        return None

def start_farming(token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.post(f"{BASE_URL}/start", headers=headers)
    if response.status_code == 200:
        logger.info("Farming started successfully")
        return response.json()
    else:
        logger.error("Failed to start farming")
        return None
