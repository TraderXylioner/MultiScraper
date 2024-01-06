import asyncio
import time

from type import Proxy, Service, Task
from utils import Parser

parser = Parser()
parser.proxies.add(Proxy('HTTP', 'localhost'))
parser.services.add(Service('binance', 100))
parser.services.add(Service('okx', 50))



async def main():
    tasks = [Task(f'http://127.0.0.1:8000/products/binance{i}', 'binance') for i in range(100)]
    print('start')
    await parser.run_manager()  # проверка запущенного менеджера
    await parser.run_tasks(tasks)
    for task in tasks:
        print(task.response)

asyncio.run(main())
