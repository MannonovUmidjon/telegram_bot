from aiogram import Bot, Dispatcher, executor
from handlers import start, language, message_forwarder
import config

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

start.register_handlers(dp)
language.register_handlers(dp)
message_forwarder.register_handlers(dp)

if __name__ == "__main__":
    print("Bot ishga tushdi!")
    executor.start_polling(dp, skip_updates=True)