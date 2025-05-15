from pydantic_settings import BaseSettings
from dotenv import dotenv_values

env = dotenv_values(".env")

class Settings(BaseSettings):
    API_KEY: str = env["API_KEY"]



settings = Settings()