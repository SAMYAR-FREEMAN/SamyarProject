from fastapi import APIRouter, Depends, HTTPException
from validators.loginValidator import loginValidator,getLoginDataFromForm
from controllers.userController import login_user

authRouter = APIRouter()

@authRouter.post("/auth/login")
async def login(loginData:loginValidator = Depends(getLoginDataFromForm)):
    return login_user(dict(loginData))