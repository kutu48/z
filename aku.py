# script.py
import time
from utils.blum import authenticate, get_user_data, claim_rewards, start_farming

def main():
    authenticate()
    username, balance = get_user_data()
    if username and balance:
        print(f"Username: {username}, Balance: {balance}")
    else:
        print("Failed to get user data")

    if claim_rewards():
        print("Claim successful")
    else:
        print("Claim failed")

    time.sleep(8 * 3600)  # Sleep for 8 hours

    if start_farming():
        print("Start farming successful")
    else:
        print("Start farming failed")

if __name__ == "__main__":
    while True:
        main()
        time.sleep(8 * 3600)
