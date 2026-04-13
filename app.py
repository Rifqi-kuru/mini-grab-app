from enum import Enum

class VehicleType(Enum):
    BIKE = 1
    CAR = 2

RATE_BIKE = 2000
RATE_CAR = 5000

def calculate_fare(distance_km, vehicle_type):
    if vehicle_type == VehicleType.BIKE:
        return distance_km * RATE_BIKE
    return distance_km * RATE_CAR

def display_order_summary(customer_name, fare):
    print(f"Customer Name: {customer_name}")
    print(f"Total Fare: Rp{fare}")

# Main Execution
customer = "Budi"
fare = calculate_fare(10, VehicleType.BIKE)
display_order_summary(customer, fare)