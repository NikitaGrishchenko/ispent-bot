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
    try:
        category_user = await services.create_category_user(
            message.from_user["id"], data["kind"], data["name"]
        )
    except Exception as e:
        await message.answer(
            "Не удалось создать категорию, возможно она уже существует, попробуйте еще раз"
        )
    if category_user:
        await message.answer("Успешно", reply_markup=types.ReplyKeyboardRemove())
    await state.finish()
