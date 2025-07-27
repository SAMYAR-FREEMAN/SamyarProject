from fastapi import APIRouter, Depends, Header, HTTPException
from validators.clotheValidator import ClotheValidator, getclotheDataFromForm
from controllers.clotheController import (
    save_clothe,
    edit_clothe,
    get_all_clothes,
    delete_clothe_with_id
)

clotheRouter = APIRouter()


@clotheRouter.get("/clothes")
async def get_clothes(page: int = 1, limit: int = 4, jwt_token: str = Header(None)):
    
    return get_all_clothes(page, limit)

@clotheRouter.post("/clothes")
async def create_clothe(clotheData: ClotheValidator = Depends(getclotheDataFromForm)):
    return save_clothe(clotheData)

@clotheRouter.put("/clothes/{id}")
async def update_clothe(id: str, clotheData: ClotheValidator = Depends(getclotheDataFromForm)):
    return edit_clothe(id, clotheData)

@clotheRouter.delete("/clothes/{id}")
async def delete_clothe(id: str):
    return delete_clothe_with_id(id)
