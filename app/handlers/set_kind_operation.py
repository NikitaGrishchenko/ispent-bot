from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from utils import states


@dp.message_handler(state=states.CreateOperation.kind)
async def set_kind_operation(message: types.Message, state: FSMContext):
    if message["text"] in ["Доход", "Расход"]:
        async with state.proxy() as data:
            data["kind"] = message["text"]
        await states.CreateOperation.category.set()
    else:
        await state.finish()
        await message.answer("Неверные данные")
