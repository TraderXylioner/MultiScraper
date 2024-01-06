import asyncio

import aiohttp

from type import Proxy, Task, ProxyManager, ServiceManager


# decomposition
class Parser:
    def __init__(self,
                 proxies: ProxyManager | None = None,
                 services: ServiceManager | None = None):
        self.proxies = proxies if proxies else ProxyManager()
        self.services = services if services else ServiceManager()
        self.work = {}

    def __repr__(self):
        return f'proxies: {self.proxies}, ' \
               f'services: {self.services}'

    def _check_data(self):
        self.proxies.check_data()
        self.services.check_data()

    def create_work(self):
        for proxy in self.proxies:
            self.work[proxy] = {service.name: service.rate_limit for service in self.services}

    async def updating_work(self):
        while True:
            await asyncio.sleep(1)
            self.create_work()

    async def run_tasks(self, tasks: list[Task]):
        tasks = [asyncio.create_task(self.send_request(task)) for task in tasks]
        for task in tasks:
            # await self.send_request(task)
            await task
        return task

    async def run_manager(self):
        self._check_data()
        self.create_work()
        asyncio.create_task(self.updating_work())

    async def get_proxy(self, task: Task):
        while True:
            base_limit = 0
            res = None
            for proxy in self.work:
                limit = self.work[proxy].get(task.service)
                if limit is None:
                    raise ValueError(f'service "{task.service}" not found')
                if limit > base_limit:
                    base_limit = limit
                    res = proxy
            if base_limit > 0:
                self.work[res][task.service] -= 1
                task.proxy = res
                break
            else:
                await asyncio.sleep(0.1)

    async def send_request(self, task: Task):
        attempts = 0
        while attempts < 10:
            try:
                await self.get_proxy(task)
                async with aiohttp.ClientSession(trust_env=True) as session:
                    async with session.get(url=task.url, proxy=task.proxy.to_string(), ssl=True) as response:
                        task.response = await response.json()
                        break
            except Exception as ex:
                raise ex
