import time
from utils.blum import BlumAPI

def main():
    with open('api.txt', 'r') as file:
        api_id, api_hash = file.read().splitlines()

    blum_api = BlumAPI(api_id, api_hash)

    if blum_api.authenticate():
        print("Authenticated successfully")

        username, balance = blum_api.get_user_info()
        if username and balance:
            print(f"Username: {username}, Balance: {balance}")

            if blum_api.claim_rewards():
                print("Claim successful")
            else:
                print("Claim failed")

            print("Waiting for 8 hours to start farming...")
            time.sleep(8 * 3600)

            if blum_api.start_farming():
                print("Farming started successfully")
            else:
                print("Failed to start farming")
        else:
            print("Failed to get user information")
    else:
        print("Authentication failed")

if __name__ == '__main__':
    main()