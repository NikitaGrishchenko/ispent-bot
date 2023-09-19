import re

import services
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from utils import keyboards, states


@dp.message_handler(state=states.ChangeDateOperation.date)
async def set_date_operation(message: types.Message, state: FSMContext):
    if (
        re.fullmatch(r"^\d{2}.\d{2}.\d{4}", message["text"])
        or re.fullmatch(r"^\d{2}.\d{2}.\d{2}", message["text"])
        or re.fullmatch(r"^\d{2}.\d{2}", message["text"])
        or message["text"].lower() in ["вчера", "позавчера"]
    ):
        data = await state.get_data()
        if data["telegram_id"]:
            await services.change_date_last_operation(data["telegram_id"], message)
            await state.finish()

    else:
        await state.finish()
        await message.answer("Неверные данные")
