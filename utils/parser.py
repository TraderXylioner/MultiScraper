import asyncio

import aiohttp

from type import Request, Task
from utils.manager import Manager


class Parser:
    def __init__(self, manager: Manager):
        self.manager = manager

    async def run_task(self, task: Task):
        task = [asyncio.create_task(self.send_request(req)) for req in task]
        for req in task:
            # await self.send_request(task)
            await req
        return task

    async def send_request(self, request: Request):
        attempts = 0
        while attempts < 10:
            try:
                await self.manager.get_proxy(request)
                async with aiohttp.ClientSession(trust_env=True) as session:
                    async with session.get(url=request.url, proxy=request.proxy.to_string(), ssl=True) as response:
                        request.response = await response.json()
                        print(request.response)
                        break
            except Exception as ex:
                raise ex
