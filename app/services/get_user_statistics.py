from aiogram import types
from utils.models import Operation, User

from .get_user import get_user


async def get_user_statistics(message: types.Message):
    """
    Get user statistics from database by tg user id
    """
    user = await get_user(message.from_user["id"])
    if user:
        user_statistics = await Operation.query.where(
            Operation.user_id == user.id
        ).gino.all()

        return user_statistics
    return None
