from type import Proxy


class ProxyManager:
    def __init__(self, proxies: list[Proxy] | None = None):
        self.proxies = proxies if proxies else []

    def add(self, proxy: Proxy):
        self.proxies.append(proxy)

    def remove(self, proxy: Proxy):
        self.proxies.remove(proxy)

    def __repr__(self):
        return f'{self.proxies}'

    def __len__(self):
        return len(self.proxies)

    def __getitem__(self, index):
        return self.proxies[index]

    def __setitem__(self, index, value):
        self.proxies[index] = value

    def __delitem__(self, index):
        del self.proxies[index]

    def _check_data(self):
        if not self.proxies:
            raise ValueError('Proxy not specified')
