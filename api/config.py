from dotenv import load_dotenv
load_dotenv()
from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    
    app_name: str= "Smart Irrigation App"
    DB_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_nested_delimiter = "__"

# print(os.getenv("DB_URL"))

settings = Settings(_env_file= os.path.join(os.getcwd(), "api/.env"))