import logging

import config
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# from aiogram.contrib.fsm_storage.redis import RedisStorage2

logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()

# storage = RedisStorage2(
#     host=REDIS_HOST,
#     port=REDIS_PORT,
#     db=REDIS_DB,
#     password=REDIS_PASSWORD,
#     # и т.д.
# )

# Данные redis-клиента
# REDIS_HOST = 'localhost'
# REDIS_PORT = 6379
# По умолчанию пароля нет. Он будет на сервере
# REDIS_PASSWORD = None

bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot=bot, storage=MemoryStorage())

__all__ = (
    "bot",
    "storage",
    "dp",
)
