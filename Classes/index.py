from Car import Car
from HybridCar import HybridCar

car1 = Car("360 Modena", "Ferrari", 6, 400, False)
car2 = Car("Gallardo", "Lamborghini", 6, 520, False)

print(car1.model)
print(car2.brand)
print(car2.horse_power)

print(car1.is_modern())

car2.add_power(150)
print(car2.horse_power)

car3 = HybridCar("Fusion Hybrid", "Ford", 6, 156, False)

print(car3.model)

car3.set_battery_duration(8)
print(car3.battery_duration)

car3.add_power(40)
print(car3.horse_power)