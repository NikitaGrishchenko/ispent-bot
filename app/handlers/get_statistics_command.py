import statistics

import services
from aiogram import types
from loader import dp
from utils.filters import IsAuth


@dp.message_handler(IsAuth(is_auth=True), commands="get_statistics")
async def get_statistics_command(message: types.Message):
    """
    This handler will be called when user sends `/get_statistics` command
    """
    user_statistics = await services.get_user_statistics(message)
