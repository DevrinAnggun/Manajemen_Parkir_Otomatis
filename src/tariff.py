from datetime import datetime, timedelta

from config import Config

class TariffCalculator:
    def __init__(self):
        self.start_time = {}
    
    def check_in(self, plate_number):
        self.start_time[plate_number] = datetime.now()
    
    def calculate_fee(self, plate_number, vehicle_type):
        if plate_number not in self.start_time:
            return 0
        duration = datetime.now() - self.start_time[plate_number]
        hours = max(1, duration.total_seconds() // 3600)
        return hours * Config.TARIFFS[vehicle_type]