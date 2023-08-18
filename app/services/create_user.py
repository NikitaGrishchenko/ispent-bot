from aiogram import types
from utils.models import User

from .get_user import get_user


async def create_user(message: types.Message):
    """
    Create user in database
    return User object
    """
    user = await get_user(message.from_user["id"])
    if user:
        await message.answer("Вы уже зарегистрированы")
    else:
        user = await User.create(
            id_telegram=message.from_user["id"],
            first_name=message.from_user["first_name"],
            username=message.from_user["username"],
            language_code=message.from_user["language_code"],
            is_bot=message.from_user["is_bot"],
        )
        return user
