from starlette.config import  Config
from starlette.datastructures import Secret

try:
    config=Config(".env")
except FileNotFoundError:
    config=Config(default_load=True)

DATABASE_URL=config("DATABASE_URL", cast=Secret)