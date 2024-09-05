from dotenv import load_dotenv
load_dotenv()
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Smart Irrigation API"
    db_connection_url: str 
    weather_api_url: str
    weather_api_key: str

    class Config:
        env_nested_delimiter = "__"


settings = Settings(_env_file=".env")
