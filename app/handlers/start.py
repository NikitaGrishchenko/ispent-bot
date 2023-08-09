from aiogram import types
from loader import dp
from services import create_user, get_user


@dp.message_handler(commands="start")
async def start(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    user = await get_user(message.from_user["id"])
    if user:
        await message.reply("Вы уже зарегистрированы")
    else:
        user = await create_user(message)
        if user:
            await message.reply("Регистрация прошла успешно")
