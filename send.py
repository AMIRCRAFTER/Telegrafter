import requests

TOKEN = input("inter your bot token:")
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

chat_id = input("inter the chat id: ")

text = input("inter your massage to send: ")

data = {'chat_id': chat_id, 'text': text}
response = requests.post(BASE_URL, data=data)

if response.status_code == 200:
    print("massage sending was succesfuly!")
else:
    print("error!?!?!?£¢€¥&", response.text)
