from aiogram import types
from loader import dp
from services import create_operation


@dp.message_handler()
async def text_handler(message: types.Message):
    await create_operation(message)
