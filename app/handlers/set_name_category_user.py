import services
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from utils import keyboards, states


@dp.message_handler(state=states.CreateCategoryUser.name)
async def set_name_category_user(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message["text"]
    data = await state.get_data()
    await message.answer(data)
    await state.finish()
