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
