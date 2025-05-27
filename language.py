from aiogram import types
from aiogram.dispatcher import Dispatcher
from config import LANGUAGES
import json, os

LANG_FILE = "telegram_bot/data/languages.json"

def load_languages():
    try:
        with open(LANG_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_languages(data):
    with open(LANG_FILE, "w") as f:
        json.dump(data, f)

def register_handlers(dp: Dispatcher):
    @dp.message_handler(lambda message: message.text in LANGUAGES.keys())
    async def set_language(message: types.Message):
        user_langs = load_languages()
        user_langs[str(message.from_user.id)] = LANGUAGES[message.text]
        save_languages(user_langs)
        await message.answer(f"Siz tanlagan til: {message.text}")