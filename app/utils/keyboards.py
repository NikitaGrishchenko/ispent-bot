import services
from aiogram.dispatcher import FSMContext
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)

cancel_last_operation_inline = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Отмена", callback_data="cancel_last_operation"),
        ]
    ],
)

kind_operation_keyboard = ReplyKeyboardMarkup(
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


async def generate_category_user_keyboard(user_id: int, state: FSMContext):
    """_summary_

    Args:
        user_id (int): _description_
        state (FSMContext): _description_

    Returns:
        _type_: _description_
    """
    data = await state.get_data()
    categories_user = await services.get_categories_user(user_id, data["kind"])
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = [item.name for item in categories_user]
    keyboard.add(*buttons)
    return keyboard
