import requests
import time
import os
from dotenv import load_dotenv
import telegram

load_dotenv()

API_KEY = os.getenv("API_KEY")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = telegram.Bot(token=BOT_TOKEN)

def fetch_otps():
    try:
        response = requests.get("http://109.236.84.81/ints", headers={"X-API-KEY": API_KEY})
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch OTPs: {response.status_code}")
            return []
    except Exception as e:
        print(f"Error fetching OTPs: {e}")
        return []

sent_ids = set()

while True:
    otps = fetch_otps()
    for otp_data in otps:
        otp_id = otp_data.get("id")
        if otp_id not in sent_ids:
            message = f"🕒 Time: {otp_data.get('time')}\n⚙️ Service: {otp_data.get('service')}\n☎️ Number: {otp_data.get('number')}\n🔑 OTP: {otp_data.get('otp')}"
            bot.send_message(chat_id=CHAT_ID, text=message)
            sent_ids.add(otp_id)
    time.sleep(10)
