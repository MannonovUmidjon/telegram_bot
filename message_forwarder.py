from aiogram import types, Dispatcher
from config import ADMINS

def register_handlers(dp: Dispatcher):
    @dp.message_handler(content_types=types.ContentType.TEXT)
    async def handle_user_message(message: types.Message):
        for admin_id in ADMINS:
            await dp.bot.send_message(
                admin_id,
                f"""Yangi xabar:
{message.text}

From: {message.from_user.full_name} (ID: {message.from_user.id})"""
            )
        await message.reply("Xabaringiz adminga yuborildi. Tez orada siz bilan bog'lanamiz.")
