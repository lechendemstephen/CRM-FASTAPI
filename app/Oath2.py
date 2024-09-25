from .config import setting
from jose import jwt, JWTError
from datetime import datetime, timedelta

# requirements to create an access token 
# SECRET_KEY
#ALGORITHM 
# ACCESS_TOKEN_EXPIRE MINUTES 

def create_acces_token(data: dict): 
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=setting.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, setting.SECRET_KEY, algorithm=setting.ALGORITHM)

    return encoded_jwt 