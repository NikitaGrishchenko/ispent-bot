from utils import models

from .get_user import get_user


async def delete_last_operation(id_telegram: int):
    """
    Delete last user operation from database by user id
    """
    user = await get_user(id_telegram)
    if user:
        operation = await models.Operation.query.where(
            models.Operation.user_id == user.id
        ).gino.first()
        await operation.delete()
