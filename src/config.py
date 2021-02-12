from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    client_secret_key: str

    class Config:
        env_file = ".env"

@lru_cache()
def get_config():
    return Settings()

