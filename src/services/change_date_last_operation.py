import datetime
import re

import emoji
import pytz
from aiogram import types
from utils import models

from .get_user import get_user


async def change_date_last_operation(telegram_id: int, message: types.Message):
    """
    Change date last user operation from database
    """
    user = await get_user(telegram_id)
    date_time_str = message["text"]
    if user:
        if re.fullmatch(r"^\d{2}.\d{2}.\d{4}", date_time_str):
            new_date = datetime.datetime.strptime(date_time_str, "%d.%m.%Y")
        if re.fullmatch(r"^\d{2}.\d{2}.\d{2}", date_time_str):
            new_date = datetime.datetime.strptime(date_time_str, "%d.%m.%y")
        if re.fullmatch(r"^\d{2}.\d{2}", date_time_str):
            date_time_str += f".{datetime.date.today().year}"
            new_date = datetime.datetime.strptime(date_time_str, "%d.%m.%Y")
        if date_time_str.lower() == "вчера":
            new_date = datetime.date.today() - datetime.timedelta(days=1)
        if date_time_str.lower() == "позавчера":
            new_date = datetime.date.today() - datetime.timedelta(days=2)

        all_operation = await models.Operation.query.where(
            models.Operation.user_id == user.id
        ).gino.all()

        all_operation_id_list = [item.id for item in all_operation]

        operation = await models.Operation.query.where(
            models.Operation.id == max(all_operation_id_list)
        ).gino.first()

        await operation.update(date=new_date).apply()

        await message.answer(
            f"Успешно {emoji.emojize(':check_mark_button:')}",
        )
