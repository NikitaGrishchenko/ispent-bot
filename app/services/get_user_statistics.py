from aiogram import types
from utils.models import Operation

from .get_user import get_user


def convert_kind_operation(kind):
    """_summary_

    Args:
        kind (_type_): _description_

    Returns:
        _type_: _description_
    """
    if kind == 0:
        return "Расход"
    else:
        return "Доход"


async def get_user_statistics(message: types.Message):
    """
    Get user statistics from database by tg user id
    """
    user = await get_user(message.from_user["id"])
    if user:
        user_statistics = await Operation.query.where(
            Operation.user_id == user.id
        ).gino.all()

        result_str = ""
        for _ in user_statistics:
            result_str += f"{_.category}, {convert_kind_operation(_.kind)}, {_.amount} руб., {_.created_at.strftime('%d/%m/%Y')} \n"
        await message.answer(result_str)
    return None
