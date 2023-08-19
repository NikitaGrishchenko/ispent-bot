import emoji
import services
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from utils import keyboards, states


@dp.message_handler(state=states.CreateCategoryUser.name)
async def set_name_category_user(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message["text"]
    data = await state.get_data()
    category_user = await services.create_category_user(
        message.from_user["id"], data["kind"], data["name"]
    )
    if category_user:
        await message.answer(
            f"Успешно {emoji.emojize(':check_mark_button:')}",
            reply_markup=types.ReplyKeyboardRemove(),
        )
    else:
        await message.answer(
            "Не удалось создать категорию, возможно она уже существует, попробуйте еще раз"
        )
    await state.finish()
