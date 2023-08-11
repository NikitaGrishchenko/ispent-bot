from utils import CategoryUser


async def get_categories_user(id_user: int):
    """
    Get categories user from database by user id
    return categories list or None
    """
    try:
        categories_user = await CategoryUser.query.where(
            CategoryUser.user_id == id_user
        ).gino.all()
        print(categories_user)
        return categories_user
    except Exception as e:
        await message.reply(e)
