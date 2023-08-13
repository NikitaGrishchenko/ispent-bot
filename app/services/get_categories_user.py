from utils import models


async def get_categories_user(id: int, kind: str):
    """
    Get categories user from database by user id
    return categories list or None
    """
    try:
        kind_number = 0 if kind == "Расход" else 1
        categories_user = (
            await models.CategoryUser.query.where(models.CategoryUser.user_id == id)
            .where(models.CategoryUser.kind == kind_number)
            .gino.all()
        )
        return categories_user
    except Exception as e:
        await message.reply(e)
