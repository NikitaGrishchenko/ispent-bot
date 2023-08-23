import emoji
import services
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp


@dp.callback_query_handler(lambda call: call.data == "cancel_last_operation")
async def cancel_last_user_operation(
    callback_query: types.CallbackQuery, state: FSMContext
):
    """_summary_

    Args:
        callback_query (types.CallbackQuery): _description_
        state (FSMContext): _description_
    """
    data = await state.get_data()
    if data["telegram_id"]:
        await services.delete_last_operation(data["telegram_id"])

        await callback_query.message.answer(
            f"Операция удалена {emoji.emojize(':prohibited:')}"
        )

        await callback_query.answer()

        await callback_query.message.delete()

        await state.finish()
