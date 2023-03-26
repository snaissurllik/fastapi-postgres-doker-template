from fastapi import APIRouter, Request


router = APIRouter(prefix="/router")


@router.get("/")
async def router_ep(request: Request):
    return await request.app.conn.fetch("SELECT * FROM mock_table")
