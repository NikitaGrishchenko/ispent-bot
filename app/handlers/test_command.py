import services
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from utils.filters import IsAuth


@dp.message_handler(IsAuth(is_auth=True), commands="test")
async def test_command(message: types.Message, state: FSMContext):
    await message.answer("1")
