from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

StatusRouter = APIRouter(
    prefix="", tags=["status"]
)

@StatusRouter.get("/")
async def status():
    return {"message": "Ok"}