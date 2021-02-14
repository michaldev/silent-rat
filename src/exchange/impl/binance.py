import json

import websocket

from binance.client import Client
from binance.enums import SIDE_BUY, ORDER_TYPE_MARKET, SIDE_SELL

from ..exchange import Exchange
from ..exchange_message import ExchangeMessage


class Binance(Exchange):
    SOCKET = "wss://stream.binance.com:9443/ws/reefusdt@kline_1m"
    client = None

    async def connect(self, api_key: str, api_secret: str):
        self.client = Client(api_key, api_secret)

    async def buy(self, quantity: str, symbol: str, price: float):
        self.client.create_order(symbol=symbol,
                                 side=SIDE_BUY,
                                 type=ORDER_TYPE_MARKET,
                                 quantity=quantity)

    async def sell(self, quantity: str, symbol: str, price: float):
        self.client.create_order(symbol=symbol,
                                 side=SIDE_SELL,
                                 type=ORDER_TYPE_MARKET,
                                 quantity=quantity)

    async def start_socket(self):
        ws = websocket.WebSocketApp(self.SOCKET, on_message=self.on_message)
        ws.run_forever()

    async def on_message(self, ws, message) -> ExchangeMessage:
        json_message = json.loads(message)

        print(json_message)

        candle = json_message['k']
        is_candle_closed = candle['x']
        close = candle['c']

        return ExchangeMessage(symbol='REEFUSDT', is_candle_closed=is_candle_closed, close=close)
