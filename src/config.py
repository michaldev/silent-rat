from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    client_secret_key: str
    telegram_api_id: int
    telegram_api_hash: str
    telegram_receiver_username: str
    binance_api_key: str
    binance_api_secret: str


@lru_cache()
def get_config():
    return Settings()

