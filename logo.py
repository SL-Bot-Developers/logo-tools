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


caption = """
✍️ Logo Created Successfully✅

◇───────────────◇

🚀 **Created By** : **[LOGO GENERATE BOT 🔅](https://t.me/The_logo_generate_bot)**

🌺 **Requestor** : ** {} **

🍀 **Powered By **  : **[🍀 zoneunlimited 🍀 ](https://t.me/zoneunlimited)**

◇───────────────◇️  
    """
#◇───────────────────────────────────────◇ 

START_BUTTONS=[
    [
        InlineKeyboardButton('🍀 Update Channel 🍀', url='https://t.me/zoneunlimited'),
        InlineKeyboardButton('🚀 Support Group 🚀', url='https://t.me/zoneunlimitedchat'),
    ],
    [InlineKeyboardButton('🌷 Github Repository 🌷', url='https://github.com/zoneunlimited/logo-tools')],
]

#◇───────────────────────────────────────◇ 

@logo.on_message(filters.command("start"))
async def start(client,message):
    await message.reply_text("🍀 Hi I am Logo Generate Bot Telegram...",
    reply_markup=START_BUTTONS)

#◇───────────────────────────────────────◇ 

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

#◇────────────────────────────────────◇ 
  
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

#◇──────────────────────────────────────◇ 

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

#◇───────────────────────────────────────────◇

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


logo.run()
