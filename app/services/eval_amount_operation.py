import re

import pandas
from aiogram import types
from aiogram.dispatcher import FSMContext
from utils import states
from utils.keyboards import create_operation_keyboard


async def eval_amount_operation(message: types.Message, state: FSMContext):
    """
    Create operation in database
    return Operation object
    """
    if re.findall(r"[^0-9+-/*.() ]", message["text"]) == []:
        try:
            result = pandas.eval(message["text"])
            await state.update_data(amount=result)
            await message.answer(
                "Выберите тип операции", reply_markup=create_operation_keyboard
            )
            # await states.CreateOperation.kind.set()
        except Exception as e:
            await message.answer(e)
