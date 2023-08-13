import services
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp


@dp.message_handler(commands="test")
async def test(message: types.Message, state: FSMContext):
    try:
        # markup = types.ReplyKeyboardRemove()
        data = await state.get_data()
        # await message.answer(message.from_user)
        await message.answer(data)
    except Exception as e:
        pass

    # await state.finish()

    # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # buttons = ["Вар 1", "Вар 2"]
    # keyboard.add(*buttons)
    # await message.answer("Выберите вариант", reply_markup=keyboard)
