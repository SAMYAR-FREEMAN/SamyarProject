from fastapi import APIRouter,Depends,Header,UploadFile,File
from validators.userValidator import userValidator,getUserDataFromForm
from controllers.userController import save_profile_pic,decode_access_token,save_user,edit_user,get_all_users,delete_user_with_id
from controllers.authController import is_admin_or_higher
userRouter = APIRouter()

@userRouter.get("/user")
@userRouter.get("/users")
async def get_users(page:int=1,limit:int=4,jwt_token:str=Header(...)):
    user_data = is_admin_or_higher(jwt_token)
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

@userRouter.post("/change_profile")
def change_profile(img:UploadFile = File(...)):
    return save_profile_pic(img)
