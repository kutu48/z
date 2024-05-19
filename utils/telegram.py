from pyrogram import Client
from data.config import API_ID, API_HASH, SESSIONS_PATH

def send_message(session_name, chat_id, message):
    with Client(session_name, api_id=API_ID, api_hash=API_HASH, workdir=SESSIONS_PATH) as app:
        app.send_message(chat_id, message)
