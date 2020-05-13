from Car import Car

car1 = Car("360 Modena", "Ferrari", 6, 400, False)
car2 = Car("Gallardo", "Lamborghini", 6, 520, False)

print(car1.model)
print(car2.brand)
print(car2.horse_power)

print(car1.is_modern())

car2.add_power(150)
print(car2.horse_power)
