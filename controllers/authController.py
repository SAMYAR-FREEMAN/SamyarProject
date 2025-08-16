from controllers.userController import decode_access_token
from fastapi import HTTPException

def is_admin_or_higher(jwt_token):
    user_data = decode_access_token(jwt_token)
    if user_data['role_name'] in ["Admin","Owner"]:
        return user_data
    else:
        raise HTTPException(status_code=403, detail="Admin or higher role required")