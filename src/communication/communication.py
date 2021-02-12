from abc import abstractmethod, ABC


class Communication(ABC):
    @property
    def client(self):
        raise NotImplementedError

    @abstractmethod
    async def initialize(self):
        raise NotImplementedError

    @abstractmethod
    async def send_message(self, message: str):
        raise NotImplementedError
