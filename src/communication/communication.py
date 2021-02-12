from abc import abstractmethod, ABC

class Communication(ABC):
    @abstractmethod
    async def initialize():
        raise NotImplementedError

    @abstractmethod
    async def send_message(message: str):
        raise NotImplementedError

