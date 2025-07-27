from fastapi import APIRouter,Depends,Header
from validators.userValidator import userValidator,getUserDataFromForm
from controllers.userController import decode_access_token,save_user,edit_user,get_all_users,delete_user_with_id
userRouter = APIRouter()


@userRouter.get("/users")
async def get_users(page:int=1,limit:int=4,jwt_token:str=Header(...)):
    print(decode_access_token(jwt_token))
    return get_all_users(page,limit)

@userRouter.post("/users")
async def create_user(userData:userValidator = Depends(getUserDataFromForm)):
    return save_user(userData)
    

@userRouter.put("/users/{id}")
async def update_user(id:str,userData:userValidator = Depends(getUserDataFromForm)):
    return edit_user(id,userData)
@userRouter.delete("/users/{id}")
async def delete_user(id:str):
    return delete_user_with_id(id)