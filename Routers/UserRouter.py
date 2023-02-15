from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse

# from Repositories.UserRepository import UserRepository


UserRouter = APIRouter(
    prefix="/user", tags=["users"]
)

@UserRouter.get("/")
async def status():
    return {"message": "user"}

# @UserRouter.get("/{email}")
# def get(
#     email: str, 
#     userRepository: UserRepository = Depends()
# ):
#     return userRepository.get_by_email(email).normalize()