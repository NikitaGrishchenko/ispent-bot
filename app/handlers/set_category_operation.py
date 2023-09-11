import asyncio

import emoji
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import MessageToDeleteNotFound
from loader import dp
from services import create_operation
from utils import keyboards, states


@dp.message_handler(state=states.CreateOperation.category)
async def set_category_operation(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["category"] = message["text"]
    data = await state.get_data()
    operation = await create_operation(
        message.from_user["id"], data["category"], data["kind"], data["amount"]
    )
    await state.finish()

    if operation:
        async with state.proxy() as data:
            data["telegram_id"] = message.from_id

        await message.answer(
            f"Операция добавлена {emoji.emojize(':check_mark_button:')}",
            reply_markup=types.ReplyKeyboardRemove(),
        )
        message_with_keyboard = await message.answer(
            "Нажмите, чтобы изменить последнюю операцию",
            reply_markup=keyboards.change_last_operation_inline,
        )
        await asyncio.sleep(4)
        try:
            await message_with_keyboard.delete()
        except MessageToDeleteNotFound:
            pass
