from dataclasses import dataclass


@dataclass
class Service:
    name: str
    rate_limit: int
