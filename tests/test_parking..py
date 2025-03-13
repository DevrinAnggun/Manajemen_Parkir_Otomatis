import unittest
from src.parking import ParkingLot
from src.vehicle import Vehicle

class TestParking(unittest.TestCase):
    def setUp(self):
        self.parking_lot = ParkingLot()
        self.vehicle = Vehicle("AB123CD", "mobil")

    def test_park_vehicle(self):
        result = self.parking_lot.park_vehicle(self.vehicle)
        self.assertTrue(result)

    def test_remove_vehicle(self):
        self.parking_lot.park_vehicle(self.vehicle)
        result = self.parking_lot.remove_vehicle("AB123CD")
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()