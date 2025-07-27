from models.clotheModel import clothe
from fastapi import HTTPException
from bson.objectid import ObjectId



def save_clothe(clotheData):
    try:
        clotheData = dict(clotheData)
        created_clothe = clothe(**clotheData).save()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"job":"ok","data":str(created_clothe)}

def get_all_clothes(page,limit):
    try:
        skip = (page-1)*limit
        clotheList = list(clothe.objects().skip(skip).limit(limit).as_pymongo())
        for clothe in clotheList:
            clothe['_id'] = str(clothe['_id'])
        return {"job":"ok","data":clotheList}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def edit_clothe(clothe_id,clotheData):
    try:
        clothe_u = clothe.objects(id=ObjectId(clothe_id))
        clothe_u.update(**dict(clotheData))
        return {"job":"ok","data":str(clothe_u)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def delete_clothe_with_id(clothe_id):
    try:
        clothe_d = clothe.objects(id=ObjectId(clothe_id))
        clothe_d.delete()
        return {"job":"ok","data":"clothe deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))