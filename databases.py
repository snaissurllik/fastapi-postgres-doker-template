import psycopg2
from time import sleep
from .config import POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD


def get_db_connection():
    while True:
        try:
            conn = psycopg2.connect(
                host="db",
                database=f"{POSTGRES_DB}",
                user=f"{POSTGRES_USER}",
                password=f"{POSTGRES_PASSWORD}",
            )
            return conn
        except psycopg2.OperationalError:
            print(
                "Failed to connect to the Postgres database. Retrying in 3 seconds..."
            )
            sleep(3)


conn = get_db_connection()
