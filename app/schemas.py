from pydantic import BaseModel, EmailStr



class User(BaseModel): 
    email: EmailStr
    password: str 

class Login(User): 
    pass 

class Record(BaseModel): 
    first_name: str 
    last_name: str 
    email: EmailStr 
    Phone: str 
    location: str 
    age: int 
    sex: str 
    payment_method: str 


class TokenData(BaseModel): 
    token: str 

