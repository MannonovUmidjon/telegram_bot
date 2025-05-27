from aiogram import types
from aiogram.dispatcher import Dispatcher
from config import ADMIN_IDS

def register_handlers(dp: Dispatcher):
    @dp.message_handler(lambda message: message.from_user.id not in ADMIN_IDS)
    async def forward_to_admin(message: types.Message):
        for admin_id in ADMIN_IDS:
            await dp.bot.send_message(admin_id, f"Yangi xabar: {message.text}")

{message.text}\n\nFrom: {message.from_user.full_name} (ID: {message.from_user.id})")
        await message.answer("Xabaringiz yuborildi. Rahmat!")