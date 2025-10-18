import requests

TOKEN = input("inter your bot token:")
URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

response = requests.get(URL).json()
updates = response.get('result', [])

if not updates:
    print("you have not new massages.")
else:
    for update in updates:
        msg = update.get('message')
        if msg:
            sender = msg['from'].get('first_name', 'unknown')
            text = msg.get('text', '')
            chat_id = msg['chat']['id']
            print(f"{sender} ({chat_id}) massage: {text}")
