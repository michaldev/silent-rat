from abc import abstractmethod, ABC


class Strategy(ABC):
    @abstractmethod
    def setUp(self):
        pass

    @abstractmethod
    def strategy(self):
        pass

