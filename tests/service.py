from type import Service
from utils import ServiceManager

manager = ServiceManager()

manager.add(Service('binance', 100))
manager.add(Service('okx', 100))

print(manager)
