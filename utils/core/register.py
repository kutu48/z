from pyrogram import Client
from data.config import API_ID, API_HASH, WORKDIR

def register_session(session_name):
    app = Client(session_name, api_id=API_ID, api_hash=API_HASH, workdir=WORKDIR)
    app.start()
    app.stop()
