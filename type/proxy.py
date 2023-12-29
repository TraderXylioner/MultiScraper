from dataclasses import dataclass


@dataclass
class Proxy:
    protocol: str
    ip: str
    port: int | None = None
    user: str | None = None
    password: str | None = None
