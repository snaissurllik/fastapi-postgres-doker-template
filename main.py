from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from .databases import connect_to_db
from .app.service.routers import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.conn = await connect_to_db()
    yield
    app.conn.close()


app = FastAPI(title="My app", lifespan=lifespan)
app.include_router(router)


@app.get("/")
async def index(request: Request):
    return await request.app.conn.fetch("SELECT * FROM mock_table")
