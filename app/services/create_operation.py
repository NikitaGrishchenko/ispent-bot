import re

import pandas
from aiogram import types
from utils import create_operation_keyboard


async def create_operation(message: types.Message):
    """
    Create operation in database
    return Operation object
    """
    if re.findall(r"[^0-9+-/*.() ]", message["text"]) == []:
        try:
            result = pandas.eval(message["text"])
            await message.answer(
                "Выберите тип операции", reply_markup=create_operation_keyboard
            )
        except Exception as e:
            await message.answer("Некорректный ввод")
