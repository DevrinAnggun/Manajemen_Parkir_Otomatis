from flask import Flask, jsonify, request # type: ignore
from parking import ParkingLot
from tariff import TariffCalculator
from vehicle import Vehicle

app = Flask(__name__)
parking_lot = ParkingLot()
tariff_calculator = TariffCalculator()

@app.route('/park', methods=['POST'])
def park():
    data = request.json
    vehicle = Vehicle(data['plate_number'], data['vehicle_type'])
    if parking_lot.park_vehicle(vehicle):
        tariff_calculator.check_in(vehicle.plate_number)
        return jsonify({"message": "Vehicle parked successfully"})
    return jsonify({"error": "Parking full"}), 400

@app.route('/exit', methods=['POST'])
def exit_parking():
    data = request.json
    plate_number = data['plate_number']
    vehicle_type = data['vehicle_type']
    fee = tariff_calculator.calculate_fee(plate_number, vehicle_type)
    parking_lot.remove_vehicle(plate_number)
    return jsonify({"message": "Vehicle exited", "fee": fee})

if __name__ == '__main__':
    app.run(debug=True)
