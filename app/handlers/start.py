import services
from aiogram import types
from loader import dp


@dp.message_handler(commands="start")
async def start(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    user = await services.create_user(message)
    if user:
        await message.answer("Регистрация прошла успешно")
