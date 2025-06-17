
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import subprocess
import os
from datetime import datetime

BOT_TOKEN = "7315821958:AAEIOKN4h3E4mjjG7oK5tBhf_pS-gxipSgw"

app = Client("yt_views_bot", bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply("👋 Welcome to *YT Views Bot*\!

Send me a valid YouTube video or Shorts link\.\n\n⚠️ *Important Terms & Conditions*:\n\- This bot is for educational use only\.
\- Using bots to increase YouTube views is against YouTube's ToS\.
\- We are not responsible for any misuse\.", parse_mode="MarkdownV2")

@app.on_message(filters.text & ~filters.command("start"))
def get_link(client, message):
    link = message.text.strip()
    if "youtube.com" in link or "youtu.be" in link:
        kb = [[
            InlineKeyboardButton("10 Views", callback_data=f"view_10|{link}"),
            InlineKeyboardButton("20 Views", callback_data=f"view_20|{link}")
        ],[
            InlineKeyboardButton("50 Views", callback_data=f"view_50|{link}"),
            InlineKeyboardButton("100 Views", callback_data=f"view_100|{link}")
        ]]
        message.reply("🔢 How many views do you want to simulate (educational)?", reply_markup=InlineKeyboardMarkup(kb))
    else:
        message.reply("❌ Invalid YouTube link. Please send a valid one.")

@app.on_callback_query()
def handle_callback(client, callback_query):
    data = callback_query.data.split("|")
    views = int(data[0].replace("view_", ""))
    link = data[1]

    with open("logs/requests.log", "a") as f:
        f.write(f"{datetime.now()} - {link} - {views} views\n")

    callback_query.message.reply(f"🚀 Simulating {views} views on: {link}\n⏳ Each tab will run for ~15 minutes.")
    subprocess.Popen(["python3", "simulate.py", link, str(views)])
    callback_query.answer("Started simulation!")

app.run()
