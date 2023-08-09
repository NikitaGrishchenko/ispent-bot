from aiogram import types
from utils import User

from .get_user import get_user


async def create_user(message: types.Message):
    """
    Create user in database
    return User object
    """
    user = await get_user(message.from_user["id"])
    if user:
        await message.reply("Вы уже зарегистрированы")
    else:
        try:
            user = await User.create(
                id_telegram=message.from_user["id"],
                first_name=message.from_user["first_name"],
                username=message.from_user["username"],
            )
            return user
        except Exception as e:
            await message.reply(e)
