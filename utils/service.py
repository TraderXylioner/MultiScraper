from type import Service


class ServiceManager:
    def __init__(self, services: list[Service] | None = None):
        self.services = services if services else []

    def add(self, service: Service):
        self.services.append(service)

    def __repr__(self):
        return f'{self.__dict__}'
