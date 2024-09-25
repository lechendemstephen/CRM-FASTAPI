from pydantic_settings import BaseSettings


class Settings(BaseSettings): 
    DB_NAME: str 
    DB_PASSWORD: str 
    DB_HOST: str 
    SECRET_KEY: str 
    ALGORITHM: str 
    ACCESS_TOKEN_EXPIRE_MINUTES: int 

    class Config: 
        env_file = '.env'


setting = Settings()