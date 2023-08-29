import services
from aiogram import types
from aiogram_dialog import DialogManager, StartMode
from loader import dp
from utils.filters import IsAuth
from utils.states import UserStatisticsState


@dp.message_handler(IsAuth(is_auth=True), commands="get_statistics")
async def get_statistics_command(message: types.Message, dialog_manager: DialogManager):
    """
    This handler will be called when user sends `/get_statistics` command
    """
    await dialog_manager.start(UserStatisticsState.main, mode=StartMode.NORMAL)
