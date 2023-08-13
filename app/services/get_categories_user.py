from utils import models


async def get_categories_user(id: int):
    """
    Get categories user from database by user id
    return categories list or None
    """
    try:
        categories_user = await models.CategoryUser.query.where(
            models.CategoryUser.user_id == id
        ).gino.all()
        return categories_user
    except Exception as e:
        await message.reply(e)
