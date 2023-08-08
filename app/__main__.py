import handlers
from aiogram import executor
from config import DATABASE_URL
from loader import dp
from utils import db


async def on_startup(dp):
    await db.set_bind(DATABASE_URL)
    # await db.gino.drop_all()
    # await db.gino.create_all()


async def on_shutdown(dp):
    await db.pop_bind().close()


if __name__ == "__main__":
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
    )
