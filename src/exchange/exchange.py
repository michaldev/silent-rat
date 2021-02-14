from abc import abstractmethod, ABC

from .exchange_message import ExchangeMessage


class Exchange(ABC):
    @property
    def client(self):
        raise NotImplementedError

    @abstractmethod
    async def connect(self, api_key: str, api_secret: str):
        raise NotImplementedError

    @abstractmethod
    async def buy(self, quantity: str, symbol: str, price: float):
        raise NotImplementedError

    @abstractmethod
    async def sell(self, quantity: str, symbol: str, price: float):
        raise NotImplementedError

    @abstractmethod
    async def start_socket(self):
        raise NotImplementedError

    @abstractmethod
    async def on_message(self, ws, message) -> ExchangeMessage:
        raise NotImplementedError
