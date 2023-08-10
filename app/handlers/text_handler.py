from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from services import eval_amount_operation


@dp.message_handler()
async def text_handler(message: types.Message, state: FSMContext):
    await eval_amount_operation(message, state)
