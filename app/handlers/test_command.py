from typing import Any

import services
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from utils.filters import IsAuth


@dp.message_handler(commands="test")
async def test_command(message: types.Message, state: FSMContext):
    await state.finish()
