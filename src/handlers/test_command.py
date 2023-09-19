from typing import Any

import services
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from utils import models
from utils.filters import IsAuth


@dp.message_handler(commands="test")
async def test_command(message: types.Message):
    operation = (
        await models.Operation.query.where(models.Operation.id == 1)
        .where(models.Operation.user_id == 1)
        .gino.first()
    )
    print(operation.date)
