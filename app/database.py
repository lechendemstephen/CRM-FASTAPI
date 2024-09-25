from sqlalchemy import create_engine
from .config import setting
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = f'postgresql://{setting.DB_NAME}:{setting.DB_PASSWORD}@{setting.DB_HOST}/CRM'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# starting the database 
def get_db(): 
    db = SessionLocal()
    try: 
        yield db
    finally: 
        db.close()


