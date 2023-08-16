import services
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import BoundFilter
from utils import exceptions


class IsAuth(BoundFilter):
    key = "is_auth"

    def __init__(self, is_auth: bool):
        self.is_auth = is_auth

    async def check(self, message: types.Message):
        if self.is_auth:
            user = await services.get_user(message.from_user["id"])
            if user:
                return True
            else:
                await message.answer(
                    f"Для начала работы необходимо зарегистрироваться \n/start"
                )
                raise exceptions.UnauthorisedException
