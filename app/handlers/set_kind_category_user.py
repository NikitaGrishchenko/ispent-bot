from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from utils import states


@dp.message_handler(state=states.CreateCategoryUser.kind)
async def set_kind_category_user(message: types.Message, state: FSMContext):
    if message["text"] in ["Доход", "Расход"]:
        async with state.proxy() as data:
            data["kind"] = message["text"]
        await message.answer(
            "Введите название категории, которая автоматически будет предлагаться вам при добавлении операции"
        )
        await states.CreateCategoryUser.next()
    else:
        await state.finish()
        await message.answer("Неверные данные")
