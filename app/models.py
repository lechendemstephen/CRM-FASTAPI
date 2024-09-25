from .database import Base 
from sqlalchemy import Column, String, Integer, TIMESTAMP

class Users(Base): 
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, unique=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    jioned_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=('now()'))
    