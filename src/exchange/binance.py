from binance.client import Client

from src.exchange.exchange import Exchange


class Binance(Exchange):
    client = None

    async def connect(self, api_key: str, api_secret: str):
        self.client = Client(api_key, api_secret)

    async def buy(self, price: float):
        pass

    async def sell(self, price: float):
        pass
