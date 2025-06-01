import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

API_KEY = os.getenv("g4eFcoWUgHo8T1VDQQ==")
CHAT_ID = os.getenv("1002535103722")
BOT_TOKEN = os.getenv("7612118596:AAFzuo-2q_i8oxxrd6C6a8pmx4JCBJAlwRs")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=CHAT_ID, text="Bot is running.")

def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
