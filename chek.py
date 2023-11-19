import requests
import json
from pyrogram import Client
from time import sleep

def perform_check(user, session_string, bot_token, chat_id):
    try:
        app = Client("usersession", session_string=session_string)
        app.start()
        sleep(0.2)

        for dialog in app.get_dialogs():
            chat = app.get_chat(dialog.chat.id)
            if "username" in str(chat):
                pass
            else:
                app.delete_channel(dialog.chat.id)
                requests.post(f"https://api.telegram.org/bot{bot_token}/sendmessage?chat_id={chat_id}&text=- | Done Delete_channel")

        app.stop()

    except Exception as e:
        requests.post(f"https://api.telegram.org/bot{bot_token}/sendmessage?chat_id={chat_id}&text={e}")
        print(str(e))

with open('account.txt', 'r') as g:
    users = g.read().splitlines()

with open('info.txt', 'r') as b:
    user = b.read()

count = len(users)
i = 0

info = open("info.txt",'r').read();bot_token = info.split('\n')[0];chat_id = info.split('\n')[1]

while True:
    session_string = users[i]
    perform_check(user, session_string, bot_token, chat_id)
    i += 1
    if i >= count:
        i = 0
        requests.post(f"https://api.telegram.org/bot{bot_token}/sendmessage?chat_id={chat_id}&text=The program has stopped")
        break
