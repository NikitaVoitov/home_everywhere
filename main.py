from aiogram.utils import executor
from home_everywhere.bot import *
from config import WEBHOOK_PATH
from config import WEBAPP_PORT

#executor.start_polling(bot.dp,
#                       skip_updates=True,
#                       on_shutdown=bot.on_shutdown)
executor.start_webhook(
    dispatcher=dp,
    webhook_path=WEBHOOK_PATH,
    skip_updates=True,
    on_startup=on_startup,
    on_shutdown=on_shutdown,
    host=WEBAPP_HOST,
    port=WEBAPP_PORT,
)

