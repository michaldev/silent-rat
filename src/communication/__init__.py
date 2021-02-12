from src.communication.communication import Communication
from src.communication.telegram import Telegram

initialized_communication = Telegram()


async def get_communication() -> Communication:
    return initialized_communication
