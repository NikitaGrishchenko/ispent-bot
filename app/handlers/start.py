from aiogram import types

from loader import dp


@dp.message_handler(commands="start")
async def start(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.reply(
        message.from_user["id"],
    )
