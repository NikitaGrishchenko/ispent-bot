import emoji
import services
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from utils import keyboards, states


@dp.callback_query_handler(lambda call: call.data == "change_date_last_operation")
async def change_date_last_operation(
    callback_query: types.CallbackQuery, state: FSMContext
):
    """ """
    data = await state.get_data()
    if data["telegram_id"]:
        await callback_query.answer()

        await callback_query.message.answer(
            "Укажите дату в формате 31.12.2000 или 31.12, или выберите что-то из подсказки",
            reply_markup=keyboards.date_keyboard,
        )

        await states.ChangeDateOperation.date.set()

        await callback_query.message.delete()

    else:
        await callback_query.answer()
        await state.finish()
