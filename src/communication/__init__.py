from src.communication.impl.cli import Cli
from src.communication.communication import Communication

initialized_communication = Cli()


async def get_communication() -> Communication:
    return initialized_communication
