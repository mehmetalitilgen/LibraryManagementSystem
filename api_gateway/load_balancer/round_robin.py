class RoundRobinBalancer:
    def __init__(self, services):
        self.services = services
        self.index = 0

    def get_next_service(self):
        if not self.services:
            raise Exception("No services available")
        service = self.services[self.index]
        self.index = (self.index + 1) % len(self.services)
        return service


