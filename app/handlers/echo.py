@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(
        message.text,
    )
