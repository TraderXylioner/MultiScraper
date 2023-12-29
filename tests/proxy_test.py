import asyncio
import time

from type import Proxy, Service
from utils import ProxyManager, ServiceManager

manager = ProxyManager()
print(manager)
manager.add(Proxy('HTTP', 'localhost', 8000, 'admin', 'pass'))
manager.add(Proxy('HTTP', 'localhost2', 8000, 'admin', 'pass'))

manager.services = ServiceManager([Service('binance', 100), Service('okx', 50)])


manager.start()
