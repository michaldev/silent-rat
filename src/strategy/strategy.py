from abc import abstractmethod, ABC


class Strategy(ABC):
    @abstractmethod
    def set_up(self):
        pass

    @abstractmethod
    def strategy(self):
        pass
