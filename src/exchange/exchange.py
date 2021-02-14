from abc import abstractmethod, ABC


class Exchange(ABC):
    @property
    def client(self):
        raise NotImplementedError

    @abstractmethod
    async def connect(self, api_key: str, api_secret: str):
        raise NotImplementedError

    @abstractmethod
    async def buy(self, price: float):
        raise NotImplementedError

    @abstractmethod
    async def sell(self, price: float):
        raise NotImplementedError
