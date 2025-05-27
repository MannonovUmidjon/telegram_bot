from aiogram import types
from aiogram.dispatcher import Dispatcher
from config import LANGUAGES

def register_handlers(dp: Dispatcher):
    @dp.message_handler(commands=["start", "lang"])
    async def send_welcome(message: types.Message):
        languages = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for lang in LANGUAGES.keys():
            languages.add(lang)
        await message.answer("Tilni tanlang:", reply_markup=languages)