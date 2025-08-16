from models.userModel import user
from models.roleModel import Role
from fastapi import HTTPException
from bson.objectid import ObjectId
from datetime import datetime, timedelta
from jose import jwt
from initiators.init_env import jwt_key
import shutil 
from os import getcwd,mkdir
from os.path import isdir



def save_user(userData):
    try:
        userData = dict(userData)
        if check_user_exists(userData['email']):
            raise HTTPException(status_code=400, detail="User already exists")
        
        created_user = user(**userData).save()
        return {"job": "ok", "data": str(created_user)}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def get_all_users(page,limit):
    try:
        skip = (page-1)*limit
        userList = list(user.objects().skip(skip).limit(limit).as_pymongo())
        for user in userList:
            user['_id'] = str(user['_id'])
        return {"job":"ok","data":userList}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def edit_user(user_id,userData):
    try:
        user_u = user.objects(id=ObjectId(user_id))
        user_u.update(**dict(userData))
        return {"job":"ok","data":str(user)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def delete_user_with_id(user_id):
    try:
        user_d = user.objects(id=ObjectId(user_id))
        user_d.delete()
        return {"job":"ok","data":"user deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def check_user_exists(email):
    try:
        existing_user = list(user.objects(email=email).as_pymongo())
        if len(existing_user) > 0:
            raise HTTPException(status_code=400, detail="User already exists")
        else:
            return False
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"[check_user_exists] {str(e)}")

    
def login_user(loginData):
    try:
        founded_user = list(user.objects(email=loginData['email']).as_pymongo())
        if len(founded_user) > 0 :
            founded_user = founded_user[0]
            if founded_user['password'] == loginData['password']:
                return create_access_token(founded_user)
            else:
                raise HTTPException(status_code=401, detail="رمز عبور اشتباه است")
        else:
            raise HTTPException(status_code=404, detail="کاربری با این ایمیل یافت نشد")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def create_access_token(founded_user):
    try:
        # expire_time = timedelta(days=2)
        userData = {
            "_id": str(founded_user['_id']),
            "full_name" : founded_user['full_name'],
            "email" : founded_user['email'],
        }
        access_token = jwt.encode(userData,key="mamadHasanQoli@9994444",algorithm="HS256")
        return {"job":"ok","access_token":access_token}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def decode_access_token(access_token):
    try:
        decoded_token = jwt.decode(access_token,key="mamadHasanQoli@9994444",algorithms=["HS256"])
        return decoded_token
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def create_public_folder():
    base_path = getcwd()
    public_path = f"{base_path}\\public"
    if isdir(public_path):
        return public_path
    else:
        mkdir(public_path)
        return public_path

def check_img_size(img):
    if img.content_type in ["image/jpeg","image/png","image/gif"]:
        print("here")
        if img.size > 1000 :
            print("here 2")
            raise HTTPException(status_code=400,
                                 detail="Image size should be less than 1000KB")
        else:
            return True


def save_profile_pic(img):
    try:
        if check_img_size(img):
            public_path = create_public_folder()
            img_path = f"{public_path}\\{img.filename}"
            with open(img_path,"wb") as dst_img:
                shutil.copyfileobj(img.file,dst_img)
            return {"job":"ok","message":f"image saved successfully at {img_path}"}
        else:
            return {"job":"error","message":"Invalid image format or size"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))