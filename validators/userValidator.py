from pydantic import BaseModel,Field,field_validator
from fastapi import Form,HTTPException

class userValidator(BaseModel):
    full_name:str = Field(...,
                          min_length=2,
                          max_length=20,
                          description="نام باید بین 2 تا 20 حرف باشد")
    email:str = Field(...,
                      min_length=5,
                      max_length=50,
                      description="ایمیل باید بین 5 تا 50 حرف باشد")
    password:str = Field(...,
                         min_length=8,
                         max_length=30,
                         description="پسوورد باید بین 8 تا 30 حرف باشد")
    @field_validator("email")
    def validate_email(cls, v):
        if "@" not in v:
            raise ValueError("ایمیل باید دارای @ باشد")
        return v
    
    
def getUserDataFromForm(
    full_name:str = Form(...),
    email:str = Form(...),
    password:str = Form(...)
):
    try: 
        return userValidator(full_name=full_name, email=email, password=password)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))