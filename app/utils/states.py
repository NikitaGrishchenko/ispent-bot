from aiogram.dispatcher.filters.state import State, StatesGroup


class CreateOperation(StatesGroup):
    amount = State()
    kind = State()
    category = State()
