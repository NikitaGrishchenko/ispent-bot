import services
from aiogram.dispatcher import FSMContext
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)

change_last_operation_inline = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Удалить", callback_data="cancel_last_operation"),
            InlineKeyboardButton(
                text="Изменить дату", callback_data="change_date_last_operation"
            ),
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

date_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Вчера"),
        ],
        [
            KeyboardButton(text="Позавчера"),
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
    categories_user = await services.get_categories_user_by_kind(user_id, data["kind"])
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = []
    if categories_user is not None:
        buttons = [item.name for item in categories_user]
    keyboard.add(*buttons)
    return keyboard
