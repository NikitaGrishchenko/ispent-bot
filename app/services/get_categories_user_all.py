from utils import models


async def get_categories_user_all(user_id: int):
    """
    Get categories user from database by user id
    return categories list or None
    """

    categories_user = await models.CategoryUser.query.where(
        models.CategoryUser.user_id == user_id
    ).gino.all()
    if categories_user:
        return categories_user
    return None
