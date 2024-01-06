from dataclasses import dataclass

from type import Proxy


@dataclass
class Task:
    url: str
    service: str
    response: object | None = None
    proxy: Proxy | None = None
