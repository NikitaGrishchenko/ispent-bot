from utils import models


async def get_categories_user_by_kind(user_id: int, kind: str):
    """
    Get categories user from database by user id
    return categories list or None
    """

    kind_number = 0 if kind == "Расход" else 1
    categories_user = (
        await models.CategoryUser.query.where(models.CategoryUser.user_id == user_id)
        .where(models.CategoryUser.kind == kind_number)
        .gino.all()
    )
    if categories_user:
        return categories_user
    return None
