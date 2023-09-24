import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import config

# from AiogramStorages.storages import PGStorage, SQLiteStorage


logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()
# storage = PGStorage(
#     username=config.DOCKER_DB_USER,
#     password=config.DOCKER_DB_PASSWORD,
#     host=config.TOKEN,
# )

bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot=bot, storage=storage)

__all__ = (
    "bot",
    "storage",
    "dp",
)
