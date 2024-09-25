from fastapi import APIRouter, Depends, status
from app import database, Oath2, models, schemas
from sqlalchemy.orm import Session



router = APIRouter(
    tags= ['Customer Records']
)

@router.get('/')
def all_records(): 

    return {
        "all": "all records"
    }

@router.post('/records', status_code=status.HTTP_200_OK)
def create_customer_record(request_record: schemas.Record, db: Session = Depends(database.get_db)): 

    new_record = models.CustomerRecord(
        **request_record.dict()
    )

    db.add(new_record)
    db.commit()
    db.refresh(new_record)


    return new_record