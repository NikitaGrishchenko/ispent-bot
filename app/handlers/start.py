from aiogram import types
from loader import dp
from utils import User


@dp.message_handler(commands="start")
async def start(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    user = await User.query.where(
        User.id_telegram == message.from_user["id"]
    ).gino.first()
    if user:
        await message.reply("Вы уже зарегистрированы")
    else:
        user = await User.create(
            id_telegram=message.from_user["id"],
            first_name=message.from_user["first_name"],
            username=message.from_user["username"],
        )
        if user:
            await print(user)
        await message.reply("Регистрация прошла успешно")
