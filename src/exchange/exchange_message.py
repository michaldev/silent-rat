from pydantic import BaseModel


class ExchangeMessage(BaseModel):
    symbol: str
    is_candle_closed: bool
    close: float
