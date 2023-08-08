from gino import Gino

db = Gino()


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    id_telegram = db.Column(db.Integer)
    username = db.Column(db.String(length=255))
    first_name = db.Column(db.String(length=255))
