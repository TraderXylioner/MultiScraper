import asyncio

from utils import ProxyManager, ServiceManager


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

    def check_data(self):
        self.proxies._check_data()
        self.services._check_data()

    def create_work(self):
        for proxy in self.proxies:
            self.work[proxy.ip] = {service.name: service.rate_limit for service in self.services}

    async def limit_update(self):
        while True:
            await asyncio.sleep(1)
            self.create_work()
            print(self.work)

    async def start(self):
        self.check_data()
        self.create_work()
        asyncio.create_task(self.limit_update())
