import asyncpg
from time import sleep
from .config import (
    POSTGRES_DB,
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_PORT
)


async def connect_to_db():
    sleep(3)
    return await asyncpg.connect(host="db",
                                 port=POSTGRES_PORT,
                                 user=POSTGRES_USER,
                                 password=POSTGRES_PASSWORD,
                                 database=POSTGRES_DB)
