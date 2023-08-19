import emoji
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from services import create_operation
from utils import states


@dp.message_handler(state=states.CreateOperation.category)
async def set_category_operation(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["category"] = message["text"]
    data = await state.get_data()
    operation = await create_operation(
        message.from_user["id"], data["category"], data["kind"], data["amount"]
    )
    if operation:
        await message.answer(
            f"Операция добавлена {emoji.emojize(':check_mark_button:')}",
            reply_markup=types.ReplyKeyboardRemove(),
        )
    await state.finish()
