from utils import User


async def get_user(id: int):
    """
    Get user from database by tg user id
    return User object or None
    """
    try:
        user = await User.query.where(User.id_telegram == id).gino.first()
        return user
    except:
        return None
