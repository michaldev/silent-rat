from abc import abstractmethod, ABC


class Strategy(ABC):
    @abstractmethod
    def set_up(self):
        pass

    @abstractmethod
    def strategy(self):
        pass


class RSI(Strategy):
    RSI_PERIOD = 14
    RSI_OVERBOUGHT = 70
    RSI_OVERSOLD = 30
    TRADE_SYMBOL = "REEFUSDT"

    def set_up(self):
        pass

    def strategy(self):
        pass
