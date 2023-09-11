import datetime
import re

import pytz
from utils import models

from .get_user import get_user


async def change_date_last_operation(id_telegram: int, date_time_str: str):
    """
    Change date last user operation from database
    """
    user = await get_user(id_telegram)
    if user:
        if re.fullmatch(r"^\d{2}.\d{2}.\d{4}", date_time_str):
            new_date = datetime.datetime.strptime(date_time_str, "%d.%m.%Y")
        if re.fullmatch(r"^\d{2}.\d{2}.\d{2}", date_time_str):
            new_date = datetime.datetime.strptime(date_time_str, "%d.%m.%y")
        if re.fullmatch(r"^\d{2}.\d{2}", date_time_str):
            new_date = datetime.datetime.strptime(date_time_str, "%d.%m")

        tz = pytz.timezone("Europe/Moscow")
        new_date = tz.localize(new_date)

        operation = await models.Operation.query.where(
            models.Operation.user_id == user.id
        ).gino.first()
        # TODO не правильно сохраняет дату
        await operation.update(created_at=new_date).apply()
