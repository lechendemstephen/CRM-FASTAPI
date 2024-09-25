from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, models, utils, Oath2



router = APIRouter(
    tags= ['Authentication']
)


# create a user 
@router.post('/users', status_code=status.HTTP_200_OK)
def create_user(user:schemas.User, db: Session = Depends(database.get_db)):

    # creating a hashed password 
    hashed_password = utils.password_hasher(user.password)
    user.password = hashed_password


    new_user = models.Users(
        **user.dict()
    ) 
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post('/login', status_code=status.HTTP_200_OK)
def login_user(request_user: schemas.Login, db: Session = Depends(database.get_db)): 
    user = db.query(models.Users).filter(models.Users.email == request_user.email).first()

    if user is None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'no user found with email: {request_user.email}')
    
    # verify if the entered password is correct 
    if not utils.verify_password(request_user.password, user.password): 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='incorrect password')
    # create accesss token 
    access_token = Oath2.create_acces_token({"user_id": user.id })

    return access_token 
