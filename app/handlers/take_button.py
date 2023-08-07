async def take_button(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Вар 1", "Вар 2"]
    keyboard.add(*buttons)
    await message.answer("Выберите вариант", reply_markup=keyboard)
