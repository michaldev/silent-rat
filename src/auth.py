from typing import Optional

from fastapi import Header, HTTPException

from .config import get_config


async def verify_client_key(client_secret_key: Optional[str] = Header(None)):
    if client_secret_key != get_config().client_secret_key:
        raise HTTPException(status_code=401, detail="Client secret key is invalid")
