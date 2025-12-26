import requests

BOT_TOKEN = "8071333538:AAFY4GCn-g1yCBBq29Ne9ouB4xD8T35-1oA"
CHAT_ID = "1756871195"

url = f"https://api.telegram.org/bot8071333538:AAFY4GCn-g1yCBBq29Ne9ouB4xD8T35-1oA/sendMessage"

data = {
    "chat_id": CHAT_ID,
    "text": "✅ Telegram test message from Python"
}

response = requests.post(url, data=data)
print(response.text)
