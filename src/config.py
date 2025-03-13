class Config:
    PARKING_CAPACITY = 100
    TARIFFS = {
        "motor": 2000,
        "mobil": 5000,
        "vip": 10000
    }
    
    @staticmethod
    def update_tariff(vehicle_type, new_price):
        Config.TARIFFS[vehicle_type] = new_price
    
    @staticmethod
    def update_capacity(new_capacity):
        Config.PARKING_CAPACITY = new_capacity