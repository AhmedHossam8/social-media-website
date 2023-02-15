from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse

from Repositories.UserRepository import UserRepository


UserRouter = APIRouter(
    prefix="/user", tags=["users"]
)

@UserRouter.get("/")
def get(
    email: str, 
    userRepository: UserRepository = Depends()
):
    user =  userRepository.get_by_email(email).normalize()

    if user:
        return JSONResponse(status_code=status.HTTP_200_OK, content=user)

    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"message": "Failed to Fetch User"})