from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook

from config import TOKEN
from config import WEBHOOK_URL
from config import logging
from dialogs import msg

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler()
async def test_message(message: types.Message):
    # имя юзера из настроек Телеграма
    user_name = message.from_user.first_name
    await message.answer(msg.test.format(name=user_name))

async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)

async def on_shutdown(dp):
    logging.warning('Shutting down..')
    await bot.delete_webhook()



