import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = str(os.getenv("TOKEN"))

DATABASE_URL = str(os.getenv("DATABASE_URL"))
