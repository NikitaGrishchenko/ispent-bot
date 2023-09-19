import emoji
import services
from aiogram import types
from loader import dp


@dp.message_handler(commands="start")
async def start_command(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    user = await services.create_user(message)
    if user:
        await message.answer(
            f"Регистрация прошла успешно {emoji.emojize(':check_mark_button:')} \nЧтобы сохранить первую операцию, введите сумму прямо в чат, или напишите выражение, которое необходимо рассчитать (например: 1600/7)"
        )
