import services
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp


@dp.message_handler(commands="test")
async def test(message: types.Message, state: FSMContext):
    user = await services.get_user(message.from_user["id"])
    await message.answer(user.username)
