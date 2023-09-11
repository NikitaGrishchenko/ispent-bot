import re

import pandas
from aiogram import types
from aiogram.dispatcher import FSMContext
from utils import keyboards, states


async def eval_amount_operation(message: types.Message, state: FSMContext):
    """
    Create operation in database
    return Operation object
    """

    # TODO если ввести 12.12.12 будет отъеб в eval
    if re.findall(r"[^0-9-+*.() /]", message["text"]) == []:
        try:
            result = round(pandas.eval(message["text"]), 2)
            await state.finish()
            async with state.proxy() as data:
                data["amount"] = result
            await message.answer(
                f"{result} ₽\nВыберите тип операции",
                reply_markup=keyboards.kind_operation_keyboard,
            )
            await states.CreateOperation.kind.set()

        except Exception as e:
            await state.finish()
            await message.answer(e)
