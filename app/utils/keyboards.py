import services
from aiogram.dispatcher import FSMContext
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


async def generate_category_user_keyboard(user_id: int, state: FSMContext):
    data = await state.get_data()
    categories_user = await services.get_categories_user(user_id, data["kind"])
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = [item.name for item in categories_user]
    keyboard.add(*buttons)
    return keyboard
