import os
import psycopg2
from time import sleep


POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")


while True:
    try:
        conn = psycopg2.connect(
            host="db",
            database=f"{POSTGRES_DB}",
            user=f"{POSTGRES_USER}",
            password=f"{POSTGRES_PASSWORD}",
        )
        break
    except psycopg2.OperationalError:
        print("Failed to connect to the Postgres database. Retrying in 3 seconds...")
        sleep(3)
