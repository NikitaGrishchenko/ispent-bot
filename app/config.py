import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = str(os.getenv("TOKEN"))

DATABASE_URL = str(os.getenv("DATABASE_URL"))


DEFAULT_USER_OPERATION = [
    {
        "kind": 0,
        "name": "Продукты",
    },
    {
        "kind": 0,
        "name": "Развлечения",
    },
    {
        "kind": 0,
        "name": "Прочее",
    },
    {
        "kind": 1,
        "name": "Зарплата",
    },
    {
        "kind": 1,
        "name": "Пассивный доход",
    },
    {
        "kind": 1,
        "name": "Прочее",
    },
]
