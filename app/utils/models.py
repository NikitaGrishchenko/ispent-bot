from gino import Gino
from sqlalchemy import Enum, func

db = Gino()


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.BigInteger, unique=True, primary_key=True, autoincrement=True)
    id_telegram = db.Column(db.BigInteger)
    username = db.Column(db.String(length=255))
    first_name = db.Column(db.String(length=255))
    last_name = db.Column(db.String(length=255))
    language_code = db.Column(db.String(length=255))
    is_bot = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())


class CategoryUser(db.Model):
    __tablename__ = "category_user"

    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    name = db.Column(db.String(length=255), unique=True)
    kind = db.Column(db.Integer)


# import enum
# class MessageTypes(enum.Enum):
#     income = 1
#     expense = 2


class Operation(db.Model):
    __tablename__ = "operation"

    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    category = db.Column(db.String(length=255))
    comment = db.Column(db.String(length=255))
    kind = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
