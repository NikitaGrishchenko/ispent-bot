import emoji
from aiogram import types
from aiogram.dispatcher import FSMContext
from utils import models

from .get_user import get_user


async def remove_category_user(message: types.Message, state: FSMContext):
    """
    Remove category_user in database
    """
    inpit_text = message["text"]
    if inpit_text.isdigit():
        id_category = int(message["text"])
        user = await get_user(message.from_user.id)
        category_user = (
            await models.CategoryUser.query.where(
                models.CategoryUser.user_id == user.id
            )
            .where(models.CategoryUser.id == id_category)
            .gino.first()
        )
        if category_user:
            await category_user.delete()
            await message.answer(
                f"Успешно {emoji.emojize(':check_mark_button:')}",
            )
            await state.finish()
        else:
            await message.answer(
                "Категории с таким id не существует",
            )
    else:
        await message.answer(
            "Невалидный id",
        )
