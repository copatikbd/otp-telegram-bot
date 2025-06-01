
import os
import requests
from telegram import Bot
import time
from dotenv import load_dotenv

load_dotenv()  # Load from .env

API_KEY = os.getenv('API_KEY')
API_URL = 'http://109.236.84.81/ints'
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

bot = Bot(token=BOT_TOKEN)
last_otp = None

def fetch_and_send_otp():
    global last_otp

    try:
        headers = {"Authorization": f"Bearer {API_KEY}"}
        response = requests.get(API_URL, headers=headers)

        if response.status_code == 200:
            data = response.json()

            number = data.get("Number")
            service = data.get("Service")
            otp = data.get("OTP")
            time_str = data.get("Time")

            if otp != last_otp:
                last_otp = otp

                message = (
                    f"🔐 *OTP Received!*\n"
                    f"📱 *Number:* `{number}`\n"
                    f"🛠️ *Service:* `{service}`\n"
                    f"🔑 *OTP:* `{otp}`\n"
                    f"🕒 *Time:* `{time_str}`"
                )

                bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="Markdown")
            else:
                print("➡️ পুরাতন OTP, পাঠানো হয়নি।")
        else:
            print(f"❌ API Error: {response.status_code}")

    except Exception as e:
        print("⚠️ Exception occurred:", e)

while True:
    fetch_and_send_otp()
    time.sleep(30)
