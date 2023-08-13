from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from services import get_categories_user, get_user
from utils import states


@dp.message_handler(state=states.CreateOperation.category)
async def set_category_operation(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["category"] = message["text"]
    data = await state.get_data()
    await message.answer(data)
    await state.finish()
