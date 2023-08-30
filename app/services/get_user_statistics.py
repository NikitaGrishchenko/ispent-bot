import emoji
from aiogram import types
from sqlalchemy import func
from utils.models import Operation

from .get_user import get_user


def _convert_kind_operation(kind):
    """_summary_

    Args:
        kind (_type_): _description_

    Returns:
        _type_: _description_
    """
    if kind == 0:
        return emoji.emojize(":red_circle:")
    return emoji.emojize(":green_circle:")


def _amount_operation_per_day(user_operations, day):
    amount_per_day = 0
    for operation in user_operations:
        if operation.created_at.strftime("%d.%m.%Y") == day:
            if operation.kind == 0:
                amount_per_day = amount_per_day - operation.amount
            if operation.kind == 1:
                amount_per_day = amount_per_day + operation.amount
    return amount_per_day


def _operation_per_day(user_operations, day):
    result_operations = []
    for operation in user_operations:
        if operation.created_at.strftime("%d.%m.%Y") == day:
            result_operations.append(
                {
                    "amount": operation.amount,
                    "kind": operation.kind,
                    "category": operation.category,
                    "created_at": operation.created_at,
                }
            )
    return result_operations


def _get_date_list(operations) -> list:
    """get all date in operations user

    Args:
        operations (obj)

    Returns:
        list: days
    """
    all_days = [operation.created_at.strftime("%d.%m.%Y") for operation in operations]
    unique_days = sorted(list(set(all_days)))

    return unique_days


async def get_user_statistics(user_telegram_id, date):
    """
    Get user statistics
    """
    user = await get_user(user_telegram_id)
    if user:
        user_operations = (
            await Operation.query.where(Operation.user_id == user.id)
            .where(func.date_part("month", Operation.created_at) == date.month)
            .where(func.date_part("year", Operation.created_at) == date.year)
            .order_by(Operation.created_at)
            .gino.all()
        )

        result_str = f"{date.strftime('%B %Y')}\n\n"

        if user_operations:
            days_list = _get_date_list(user_operations)

            result = []
            total_for_month = 0

            for day in days_list:
                amount_operation_per_day = _amount_operation_per_day(
                    user_operations, day
                )
                total_for_month += amount_operation_per_day
                result.append(
                    {
                        "day": day,
                        "sum": amount_operation_per_day,
                        "operations": _operation_per_day(user_operations, day),
                    }
                )

            for item in result:
                result_str += f"{item['day'][:-5]}\n"
                for operation in item["operations"]:
                    result_str += f"{_convert_kind_operation(operation['kind'])} {operation['amount']:g} ₽ — {operation['category']} \n"
                result_str += f"Итого за день: {item['sum']:g} ₽ \n\n"

            result_str += f"Итого за месяц: {total_for_month:g} ₽ "

            return result_str

        result_str += "Ничего не добавлено"

        return result_str

    return None
