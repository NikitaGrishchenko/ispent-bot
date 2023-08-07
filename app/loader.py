import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import config

logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()


bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot=bot, storage=MemoryStorage())

__all__ = (
    "bot",
    "storage",
    "dp",
)
