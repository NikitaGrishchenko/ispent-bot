from utils.models import User


async def get_user(id_telegram: str):
    """
    Get user from database by tg user id
    return User object or None
    """
    user = await User.query.where(User.id_telegram == id_telegram).gino.first()
    if user:
        return user
    return None
