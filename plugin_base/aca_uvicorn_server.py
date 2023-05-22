import asyncio
import logging
import socket
from typing import List, Optional
import uvicorn

logger = logging.getLogger("uvicorn.error")

class AzureContainerAppsUvicornServer(uvicorn.Server):
    def __init__(self, config: uvicorn.Config, shutdownStartedCallback = None) -> None:
        super().__init__(config)
        self.shutdownStartedCallback = shutdownStartedCallback

    async def shutdown(self, sockets: Optional[List[socket.socket]] = None) -> None:
        logger.info(f"Delaying shutdown for 30 seconds...")
        if self.shutdownStartedCallback is not None:
            self.shutdownStartedCallback()
        try:
            await asyncio.wait_for(self._wait_for_shutdown_delay(), timeout=30)
        except asyncio.TimeoutError:
            pass
        await super().shutdown(sockets)

    async def _wait_for_shutdown_delay(self):
        while not self.force_exit:
            await asyncio.sleep(0.1)