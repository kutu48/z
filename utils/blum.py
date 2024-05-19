import requests

class BlumAPI:
    BASE_URL = "https://game-domain.blum.codes/api/v1/farming"
    AUTH_URL = "https://gateway.blum.codes/v1/auth/provider/PROVIDER_TELEGRAM_MINI_APP"
    USER_CHECK_URL = "https://gateway.blum.codes/v1/user/me"

    def __init__(self, api_id, api_hash):
        self.api_id = api_id
        self.api_hash = api_hash
        self.session = requests.Session()
        self.auth_token = None

    def authenticate(self):
        response = self.session.post(self.AUTH_URL, json={'api_id': self.api_id, 'api_hash': self.api_hash})
        if response.status_code == 200:
            self.auth_token = response.json().get('auth_token')
            self.session.headers.update({'Authorization': f'Bearer {self.auth_token}'})
            return True
        return False

    def get_user_info(self):
        response = self.session.get(self.USER_CHECK_URL)
        if response.status_code == 200:
            user_data = response.json()
            username = user_data['username']
            balance = user_data['balance']
            return username, balance
        return None, None

    def claim_rewards(self):
        claim_url = f"{self.BASE_URL}/claim"
        response = self.session.post(claim_url)
        if response.status_code == 200:
            return True
        return False

    def start_farming(self):
        start_farming_url = f"{self.BASE_URL}/start"
        response = self.session.post(start_farming_url)
        if response.status_code == 200:
            return True
        return False
