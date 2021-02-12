from fastapi import APIRouter, Depends

from src.communication import get_communication
from src.communication.communication import Communication

router = APIRouter()


@router.post('/run_trade')
async def run_trade(communication: Communication = Depends(get_communication)):
    await communication.send_message(message='test')


