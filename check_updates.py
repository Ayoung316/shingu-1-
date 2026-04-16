import urllib.request
import json

TELEGRAM_BOT_TOKEN = '8768200515:AAFfCvsejDrc6yL1jXhXVfCC8xtNhB7Bwz8'

def get_updates():
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            if data.get("ok"):
                return data.get("result", [])
            else:
                print("Error:", data.get("description"))
                return []
    except Exception as e:
        print("Exception:", e)
        return []

if __name__ == "__main__":
    updates = get_updates()
    if not updates:
        print("최근에 봇에게 메시지를 보낸 사람이 없습니다. 텔레그램 앱에서 봇에게 메시지를 하나 보내주세요!")
    else:
        for update in updates:
            message = update.get("message", {})
            from_user = message.get("from", {})
            chat = message.get("chat", {})
            print(f"User: {from_user.get('first_name')} {from_user.get('last_name')} (@{from_user.get('username')})")
            print(f"Chat ID: {chat.get('id')}")
            print(f"Text: {message.get('text')}")
            print("-" * 20)
