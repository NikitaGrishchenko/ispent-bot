from utils.models import User


async def get_user_statistics(id_telegram: str):
    """
    Get user statistics from database by tg user id
    """
    user = await User.query.where(User.id_telegram == id_telegram).gino.first()
    if user:
        return user
    return None
