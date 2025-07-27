from pydantic import BaseModel,field_validator,EmailStr,constr
from fastapi import Form,HTTPException

class loginValidator(BaseModel):
    email: str
    password: constr(min_length=8,max_length=20) # type: ignore

    @field_validator('email')
    def email_validator(cls, v):
        if '@' not in v:
            raise ValueError('ایمیل معتبر نیست !')
        return v
    

async def getLoginDataFromForm(
        email: str = Form(...),
        password: str = Form(...),
):
    try:
        return loginValidator(email=email, password=password)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))