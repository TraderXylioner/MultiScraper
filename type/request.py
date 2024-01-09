class Request:
    def __init__(self, url: str, service: str):
        self.url = url
        self.service = service
        self.response = None
        self.proxy = None
