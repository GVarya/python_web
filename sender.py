import requests


username = input("имя ")
while True:
    text = input("текст ")


    requests.get(
    'http://127.0.0.1:5000/send_messages', json={"username": username, "text": text}
    )