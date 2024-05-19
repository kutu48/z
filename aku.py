import time
from utils.core.register import register_session
from utils.blum import authenticate, get_user_info, claim_reward, start_farming
from utils.core.logger import logger

def main():
    session_name = "session_name"
    register_session(session_name)

    token = authenticate()
    if not token:
        logger.error("Exiting due to authentication failure.")
        return

    user_info = get_user_info(token)
    if user_info:
        username = user_info.get('username')
        balance = user_info.get('balance')
        logger.info(f"Username: {username}, Balance: {balance}")

    claim_response = claim_reward(token)
    if claim_response:
        logger.info("Successfully claimed reward")

    time.sleep(8 * 60 * 60)  # Sleep for 8 hours

    farming_response = start_farming(token)
    if farming_response:
        logger.info("Successfully started farming")

if __name__ == "__main__":
    while True:
        main()
        time.sleep(30 * 60)  # Run the script every 30 minutes
