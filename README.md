```
from pyrogram import filters
from pyrogram.types import Message
from requests import get
import os
import requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

logo = Client("logo Bot", bot_token = BOT_TOKEN, api_id = API_ID, api_hash = API_HASH)

logo.run()

caption = """
✍️ Logo Created Successfully✅

◇───────────────◇

🚀 **Created By** : **[LOGO GENERATE BOT 🔅](https://t.me/The_logo_generate_bot)**

🌺 **Requestor** : ** {} **

🍀 **Powered By **  : **[🍀 zoneunlimited 🍀 ](https://t.me/zoneunlimited)**

◇───────────────◇️  
    """
#logo creator
@logo.on_message(filters.command("logo"))
async def on_off_antiarab(_, message: Message):
    text = message.text.split(None, 1)[1]
    photo = get(f"https://api.single-developers.software/logo?name={text}").history[1].url
    await app.send_photo(message.chat.id, photo=photo, caption =caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🍀 Open In Google 🍀", url=f"{photo}"
                    )
                ]
            ]
          ),
    )
#hq logo creator
@logo.on_message(filters.command("logohq"))
async def on_off_antiarab(_, message: Message):
    text = message.text.split(None, 1)[1]
    photo = get(f"https://api.single-developers.software/logohq?name={text}").history[1].url
    await app.send_photo(message.chat.id, photo=photo, caption =caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🍀 Open In Google 🍀", url=f"{photo}"
                    )
                ]
            ]
          ),
    )

#handwrite
@logo.on_message(filters.command("write"))
async def on_off_antiarab(_, message: Message):
    text = message.text.split(None, 1)[1]
    API = "https://api.single-developers.software/write"
    body = {     
     "text":f"{text}"     
    }
    req = requests.post(API, headers={'Content-Type': 'application/json'}, json=body)
    img = req.history[1].url
    await app.send_photo(message.chat.id, photo=img, caption =caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🍀 Open In Google 🍀", url=f"{img}"
                    )
                ]
            ]
          ),
    )

#wallpaper
@logo.on_message(filters.command("wall"))
async def on_off_antiarab(_, message: Message):
    text = message.text.split(None, 1)[1]
    photo = get(f"https://api.single-developers.software/wallpaper?search={text}").history[1].url
    await app.send_photo(message.chat.id, photo=photo, caption=caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🍀 Open In Google 🍀", url=f"{photo}"
                    )
                ]
            ]
          ),
    )
```
