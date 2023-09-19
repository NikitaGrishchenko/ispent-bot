import services
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from utils import keyboards, states
from utils.filters import IsAuth


@dp.message_handler(IsAuth(is_auth=True), commands="remove_category")
async def remove_category(message: types.Message, state: FSMContext):
    """
    This handler will be called when user sends `/remove_category` command

    """
    user = await services.get_user(message.from_user.id)
    user_categories = await services.get_categories_user_all(user.id)
    if user_categories is None:
        await message.answer("Свои категории отсутствуют")
    else:
        await message.answer("Введите id категории, которую хотите удалить")
        list_categories = ""
        for category in user_categories:
            list_categories += f"{category.name} — {'Доход' if category.kind == 1 else 'Расход'} — {category.id} \n"
        await message.answer(list_categories)

        await states.RemoveCategoryUser.id.set()
