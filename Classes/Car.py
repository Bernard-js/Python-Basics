class Car:
    def __init__(self, model, brand, gear_number, horse_power, has_carburetor):
        self.model = model
        self.brand = brand
        self.gear_number = gear_number
        self.horse_power = horse_power
        self.has_carburetor = has_carburetor

    def is_modern(self):
        if self.has_carburetor:
            return False
        else:
            return True

    def add_power(self, power):
        self.horse_power += power
