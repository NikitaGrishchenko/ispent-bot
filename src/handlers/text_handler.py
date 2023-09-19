import services
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from utils.filters import IsAuth


@dp.message_handler(IsAuth(is_auth=True))
async def text_handler(message: types.Message, state: FSMContext):
    await services.eval_amount_operation(message, state)
