from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from utils import keyboards, states
from utils.filters import IsAuth


@dp.message_handler(IsAuth(is_auth=True), commands="add_category")
async def add_category(message: types.Message, state: FSMContext):
    """
    This handler will be called when user sends `/add_category` command
    """
    await state.finish()
    await message.answer("Выберите тип", reply_markup=keyboards.kind_operation_keyboard)
    await states.CreateCategoryUser.kind.set()
