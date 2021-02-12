from abc import abstractmethod, ABC

class Exchange(ABC):
    @abstractmethod
    async def connect():
        raise NotImplementedError

    @abstractmethod
    async def buy(price: float):
        raise NotImplementedError

    @abstractmethod
    async def sell(price: float):
        raise NotImplementedError

