from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.batery = battery
    
    def needs_service(self):
        return self.engine.needs_service() or self.batery.needs_service()