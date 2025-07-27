from pydantic import BaseModel,Field,field_validator
from fastapi import Form,HTTPException
from enum import Enum

class SizeEnum(str, Enum):
    XS = 'XS'
    S = 'S'
    M = 'M'
    L = 'L'
    XL = 'XL'
    XXL = 'XXL'

class ClotheValidator(BaseModel):
    Size: str = Field(...)
    
    Color: str = Field(...,
                       min_length=3,
                       max_length=20,
                       description="رنگ باید بین 3 تا 20 کاراکتر باشد")
    
    Price:int = Field(...,
                      gt=1,
                      lt=1000000,
                      description="قیمت باید بین 1 تا 1000000 باشد")
    
    Height:float = Field(None,
                      gt=1,
                      lt=3,
                      description="طول باید بین 1 تا 3 متر باشد")
    

    @field_validator('Size')
    def validate_size(cls, v):
        allowed_sizes = [size.value for size in SizeEnum]
        if v not in allowed_sizes:
            raise ValueError(f"سایز وارد شده باید بین این مقدارها باشد: {', '.join(allowed_sizes)}")
        return v

def getclotheDataFromForm(
    Size:str = Form(...),
    Color:str = Form(...),
    Price:int = Form(...),
    Height:float = Form(None)
):
    try: 
        return ClotheValidator(Size = Size, Color = Color, Price = Price, Height = Height)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
