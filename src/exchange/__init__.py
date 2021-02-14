from .binance import Binance
from .exchange import Exchange

initialized_exchange = Binance()


async def get_exchange() -> Exchange:
    return initialized_exchange
