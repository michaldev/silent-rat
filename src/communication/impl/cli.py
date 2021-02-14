from ..communication import Communication


class Cli(Communication):
    client = None

    async def initialize(self):
        pass

    async def send_message(self, message: str):
        print(message)
