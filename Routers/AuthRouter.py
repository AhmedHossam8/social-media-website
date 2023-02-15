from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from Schemas.UserSchema import User
from Repositories.UserRepository import UserRepository

from Schemas.UserSchema import UserLogin
from Services.AuthService import AuthService


AuthRouter = APIRouter(
    prefix="/auth", tags=["auth"]
)

@AuthRouter.post("/login")
def get(
    user: UserLogin,
    authService: AuthService = Depends()
):
    email = user.email
    password = user.password

    is_logged = authService.login(email, password)

    if is_logged:
        return JSONResponse(status_code=status.HTTP_200_OK,content={"message": "success"})
    return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"message": "user doesn't exist"})


@AuthRouter.post("/sign-up")
def sign_up(
    user: User,
    authService: AuthService = Depends()
):
    name = user.name
    email = user.email
    password = user.password

    is_registered = authService.signUp(name, email, password)

    if is_registered:
        return JSONResponse(status_code=status.HTTP_200_OK,content={"message": "success"})

    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"message": "Failed to Register User"})