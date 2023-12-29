import asyncio
import time

from type import Proxy, Service
from utils import Parser

parser = Parser()
parser.proxies.add(Proxy('HTTP', 'localhost'))
parser.services.add(Service('site', 10))


async def main():
    await parser.start()
    await asyncio.sleep(100)


asyncio.run(main())
