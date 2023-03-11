from fastapi import FastAPI
from .config import conn


app = FastAPI(title="My app")
cur = conn.cursor()


@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}
