from fastapi import FastAPI
from Routers.StatusRouter import StatusRouter
from Routers.UserRouter import UserRouter
app = FastAPI()



app.include_router(StatusRouter)
app.include_router(UserRouter)