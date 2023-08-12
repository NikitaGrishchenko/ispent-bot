from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from services.get_categories_user import get_categories_user
from utils import states

# cat = await get_categories_user(1)


@dp.callback_query_handler()
# @dp.callback_query_handler(state=states.CreateOperation.kind)
async def callback_set_kind_operation(
    callback_query: types.CallbackQuery, state: FSMContext
):
    if callback_query.data in ["income", "expense"]:
        await state.update_data(kind=callback_query.data)
        await callback_query.answer()
        # await callback_query.message.reply(callback_query.data)
