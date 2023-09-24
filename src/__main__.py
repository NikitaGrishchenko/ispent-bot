import locale

from aiogram import executor
from aiogram_dialog import DialogRegistry

import config
import handlers
from dialogs.user_statistics_dialog import user_statistics_dialog
from loader import dp
from utils import db, set_default_commands


async def on_startup(dp):
    await db.set_bind(config.DATABASE_URL)
    await set_default_commands(dp)
    # await db.gino.drop_all()
    await db.gino.create_all()


async def on_shutdown(dp):
    await db.pop_bind().close()


if __name__ == "__main__":
    registry = DialogRegistry(dp)
    registry.register(user_statistics_dialog)

    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
    )
