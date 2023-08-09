import re

import pandas
from aiogram import types
from loader import dp


@dp.message_handler()
async def create_operation(message: types.Message):
    if re.findall(r"[^0-9+-/*.() ]", message["text"]) == []:
        try:
            result = pandas.eval(message["text"])
            await message.answer(result)
        except Exception as e:
            await message.answer(text="Некорректный ввод")
    else:
        await message.answer("Некорректный ввод")
