from fastapi import APIRouter



router = APIRouter()

@router.get('/records')
def all_records(): 

    return {
        "all": "all records"
    }