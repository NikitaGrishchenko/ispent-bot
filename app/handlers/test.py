from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp


@dp.message_handler(commands="test")
async def test(message: types.Message, state: FSMContext):
    markup = types.ReplyKeyboardRemove()
    data = await state.get_data()
    await message.answer(data, reply_markup=markup)

    # await state.finish()

    # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # buttons = ["Вар 1", "Вар 2"]
    # keyboard.add(*buttons)
    # await message.answer("Выберите вариант", reply_markup=keyboard)
