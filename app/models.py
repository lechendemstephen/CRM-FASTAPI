from .database import Base 
from sqlalchemy import Column, String, Integer, TIMESTAMP

class Users(Base): 
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, unique=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    jioned_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=('now()'))


class CustomerRecord(Base): 
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    Phone = Column(String, nullable=True)
    location = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    sex = Column(String, nullable=True)
    payment_method = Column(String, nullable=True)

    created_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=('now()'))
    