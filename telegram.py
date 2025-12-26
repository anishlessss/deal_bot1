import requests
import requests
from config import BOT_TOKEN, CHAT_ID

def send(message):
    url = f"https://api.telegram.org/bot8071333538:AAFY4GCn-g1yCBBq29Ne9ouB4xD8T35-1oA/sendMessage"
    data = {
        "chat_id": -1003563361184,
        "text": message,
        "disable_web_page_preview": False
    }
    r = requests.post(url, data=data)
    print("Telegram:", r.text)


