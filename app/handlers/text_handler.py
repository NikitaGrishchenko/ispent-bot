import services
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp


@dp.message_handler()
async def text_handler(message: types.Message, state: FSMContext):
    await services.eval_amount_operation(message, state)
