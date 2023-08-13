import services
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from utils import keyboards, states


@dp.message_handler(state=states.CreateOperation.kind)
async def set_kind_operation(message: types.Message, state: FSMContext):
    if message["text"] in ["Доход", "Расход"]:
        async with state.proxy() as data:
            data["kind"] = message["text"]
        user = await services.get_user(message.from_user["id"])
        keyboard = await keyboards.generate_category_user_keyboard(user.id)
        await message.answer("Введите категорию", reply_markup=keyboard)
        await states.CreateOperation.next()
    else:
        await state.finish()
        await message.answer("Неверные данные")
