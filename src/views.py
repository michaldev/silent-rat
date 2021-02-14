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
    await exchange.start_socket()


