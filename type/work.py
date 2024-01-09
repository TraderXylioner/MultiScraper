from dataclasses import dataclass

from type import Proxy


@dataclass
class Work:
    proxy: Proxy
    services: dict
