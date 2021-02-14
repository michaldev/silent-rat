from binance.client import Client

from fastapi import APIRouter, Depends

from .communication import get_communication
from .communication.communication import Communication
from .exchange import Exchange, get_exchange

router = APIRouter()


@router.post('/run_trade')
async def run_trade(communication: Communication = Depends(get_communication),
                    exchange: Exchange = Depends(get_exchange)):
    await communication.send_message(message='starting trading')
    hist = exchange.client.get_historical_klines("REEFUSDT", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")

    await communication.send_message(message=hist)

