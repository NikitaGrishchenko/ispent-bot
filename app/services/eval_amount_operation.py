import re

import pandas
from aiogram import types
from aiogram.dispatcher import FSMContext
from services.get_categories_user import get_categories_user
from utils.keyboards import create_operation_keyboard
from utils.states import CreateOperation


async def eval_amount_operation(message: types.Message, state: FSMContext):
    """
    Create operation in database
    return Operation object
    """
    if re.findall(r"[^0-9+-/*.() ]", message["text"]) == []:
        try:
            result = pandas.eval(message["text"])
            await state.update_data(amount=result)
            cat = await get_categories_user(1)
            # await message.answer(
            #     "Выберите тип операции", reply_markup=create_operation_keyboard
            # )
        except Exception as e:
            await message.answer(e)
