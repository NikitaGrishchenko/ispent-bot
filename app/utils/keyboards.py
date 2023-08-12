from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

create_operation_keyboard = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Доход", callback_data="income"),
        ],
        [
            InlineKeyboardButton(text="Расход", callback_data="expense"),
        ],
    ],
)
