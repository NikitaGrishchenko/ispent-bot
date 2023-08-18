from utils.models import Operation

from .get_user import get_user


async def create_operation(
    user_telegram_id: int,
    category: str,
    kind: str,
    amount: int,
):
    """
    Create operation user in database
    return Operation object
    """
    user = await get_user(user_telegram_id)
    kind_number = 0 if kind == "Расход" else 1
    operation = await Operation.create(
        user_id=user.id,
        category=category,
        kind=kind_number,
        amount=amount,
    )
    return operation
