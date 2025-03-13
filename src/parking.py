from config import Config


class ParkingLot:
    def __init__(self):
        self.occupied_slots = {}
    
    def check_availability(self):
        return len(self.occupied_slots) < Config.PARKING_CAPACITY
    
    def park_vehicle(self, vehicle):
        if self.check_availability():
            self.occupied_slots[vehicle.plate_number] = vehicle
            return True
        return False
    
    def remove_vehicle(self, plate_number):
        return self.occupied_slots.pop(plate_number, None)
