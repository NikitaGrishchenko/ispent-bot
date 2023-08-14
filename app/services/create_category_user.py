from aiogram import types
from utils import models

from .get_user import get_user


async def create_category_user(
    user_telegram_id: int,
    kind: str,
    name: str,
):
    """
    Create category_user in database
    return category_user object
    """
    user = await get_user(user_telegram_id)
    kind_number = 0 if kind == "Расход" else 1
    category_user = await models.CategoryUser.create(
        user_id=user.id,
        kind=kind_number,
        name=name,
    )
    if category_user:
        return category_user
