import logging

import config
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# from aiogram.contrib.fsm_storage.redis import RedisStorage2


logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()

# storage = RedisStorage2(
#     host=config.REDIS_HOST,
#     port=config.REDIS_PORT,
#     db=config.REDIS_DB,
# )

bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)

# dp = Dispatcher(bot=bot, storage=RedisStorage2())
dp = Dispatcher(bot=bot, storage=storage)

__all__ = (
    "bot",
    "storage",
    "dp",
)
