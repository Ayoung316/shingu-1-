import urllib.request
import json

TELEGRAM_BOT_TOKEN = '8768200515:AAFfCvsejDrc6yL1jXhXVfCC8xtNhB7Bwz8'
TELEGRAM_CHAT_ID = '8753832186'  # Trying the other ID from the text file

def send_test():
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    message = "🤖 [아이디 확인 테스트] 이 메시지가 본인의 텔레그램으로 왔다면 성공입니다!"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    data_json = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(url, data=data_json, headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
            if result.get("ok"):
                print(f"✅ ID {TELEGRAM_CHAT_ID}로 메시지 전송 성공!")
            else:
                print(f"❌ ID {TELEGRAM_CHAT_ID} 전송 실패:", result.get("description"))
    except Exception as e:
        print(f"💥 오류: {e}")

if __name__ == "__main__":
    send_test()
