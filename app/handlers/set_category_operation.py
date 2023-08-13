from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from utils import states

# cat = await get_categories_user(1)


@dp.message_handler(state=states.CreateOperation.category)
async def set_category_operation(message: types.Message, state: FSMContext):
    pass
    # if message["text"] in ["Доход", "Расход"]:
    #     async with state.proxy() as data:
    #         data["kind"] = message["text"]
    #     data = await state.get_data()
    #     await message.answer(data)
    #     await state.finish()
    #     # await state.reset_state(with_data=False)
    # else:
    #     await state.finish()
    #     await message.answer("Неверные данные")
