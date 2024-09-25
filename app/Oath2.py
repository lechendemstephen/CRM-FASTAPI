from .config import setting
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi import HTTPException, status, Depends
from .schemas import TokenData
from fastapi.security import OAuth2PasswordBearer

# requirements to create an access token 
# SECRET_KEY
#ALGORITHM 
# ACCESS_TOKEN_EXPIRE MINUTES 

oath2_schemes = OAuth2PasswordBearer(tokenUrl='login')




def create_acces_token(data: dict): 
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=setting.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, setting.SECRET_KEY, algorithm=setting.ALGORITHM)

    return encoded_jwt 

def verify_access_token(token: str , credential_exception): 
    try : 
        payload = jwt.decode(token, setting.SECRET_KEY, algorithms=setting.ALGORITHM)
    except: 
        raise credential_exception 
    id: str = payload.get('user_id')
    if id is None: 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid token id')
    token_data = TokenData(id=str(id))

    return token_data

def get_current_user(token: str = Depends(oath2_schemes)): 
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='not authorized')

    return verify_access_token(token, credential_exception)

    