from fastapi import FastAPI
from .databases import conn


app = FastAPI(title="My app")
