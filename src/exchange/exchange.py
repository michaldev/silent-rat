from abc import abstractmethod, ABC


class Exchange(ABC):
    @abstractmethod
    async def connect(self):
        raise NotImplementedError

    @abstractmethod
    async def buy(self, price: float):
        raise NotImplementedError

    @abstractmethod
    async def sell(self, price: float):
        raise NotImplementedError
