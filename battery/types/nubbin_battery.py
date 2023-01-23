from battery.battery import Battery

class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.years_for_service = 3

    def needs_service(self):
        check_date = self.last_service_date.replace(year=self.last_service_date.year + self.years_for_service)
        if check_date < self.current_date:
            return True
        else:
            return False