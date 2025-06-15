from pydantic import BaseSettings
from dotenv import load_dotenv
load_dotenv()


class Settings(BaseSettings):
    mongodb_uri: str
    db_name: str

    class Config:
        env_file = "../.env"

settings = Settings()
