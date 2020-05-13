from Car import Car


class HybridCar(Car):
    battery_power = 0
    battery_duration = 0

    def set_battery_power(self, power):
        self.battery_power = power

    def set_battery_duration(self, duration):
        self.battery_duration = duration