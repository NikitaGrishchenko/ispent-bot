import services
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from utils import keyboards, states


@dp.message_handler(state=states.RemoveCategoryUser.id)
async def set_id_category_user(message: types.Message, state: FSMContext):
    await services.remove_category_user(message, state)
