from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

create_operation_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Доход"),
        ],
        [
            KeyboardButton(text="Расход"),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
