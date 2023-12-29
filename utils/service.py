from type import Service


class ServiceManager:
    def __init__(self, services: list[Service] | None = None):
        self.services = services if services else []

    def add(self, service: Service):
        self.services.append(service)

    def remove(self, service: Service):
        self.services.remove(service)

    def __repr__(self):
        return f'{self.services}'

    def __len__(self):
        return len(self.services)

    def __getitem__(self, index):
        return self.services[index]

    def __setitem__(self, index, value):
        self.services[index] = value

    def __delitem__(self, index):
        del self.services[index]

    def check_data(self):
        if not self.services:
            raise ValueError('Service not specified')
