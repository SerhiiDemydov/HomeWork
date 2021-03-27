import time
import random


class LowBattery(Exception):
    pass


class BatteryZero(Exception):
    pass


class WaterZero(Exception):
    pass


class LowWater(Exception):
    pass


class Full(Exception):
    pass


class AlmostFull (Exception):
    pass


class VacuumCleanerRobot:
    max_battery = 100.0  # %
    max_fullness = 100.0  # %
    max_water = 100.0  # %
    currently_quantity_iter = 0

    def __init__(self, currently_battery, currently_water, currently_fullness):
        self.currently_battery = float(currently_battery)
        if self.currently_battery > self.max_battery:
            self.currently_battery = self.max_battery
        elif self.currently_battery < 0:
            self.currently_battery = 0
        self.currently_fullness = float(currently_fullness)
        if self.currently_fullness > self.max_fullness:
            self.currently_fullness = self.max_fullness
        elif self.currently_fullness < 0:
            self.currently_fullness = 0
        self.currently_water = float(currently_water)
        if self.currently_water > self.max_water:
            self.currently_water = self.max_water
        elif self.currently_water < 0:
            self.currently_water = 0

    def move(self, quantity_iter):
        print(f'Robot starts to move with level battery = {self.currently_battery}%')
        print(f'Robot starts to wash with water level = {self.currently_water}%')
        print(f'Robot starts to clean with fullness level = {self.currently_fullness}%\n\n')

        while self.currently_quantity_iter < int(quantity_iter):
            self.currently_quantity_iter += 1
            print(f'---------Iteration {self.currently_quantity_iter}---------')
            try:
                self.currently_battery -= random.randrange(3, 9, 1)
                if self.currently_battery <= 20:
                    if self.currently_battery < 0:
                        raise BatteryZero("Battery level is zero")
                    raise LowBattery(f"Battery very low: {self.currently_battery}%")
                print(f'Robot moves with level battery = {self.currently_battery}%')
            except(LowBattery,):
                print(f"The robot has a very low battery level: {self.currently_battery}%")
            except(BatteryZero,):
                print("The robot is discharged")
                break

            try:
                self.__wash()
            except(WaterZero,):
                print("The water has run out. Wash dont work")
            except(LowWater,):
                print(f"The water is almost over ({self.currently_water}%). Top it up")

            try:
                self.__vacuum_cleaner()
            except(AlmostFull,):
                print(f"The trash bin is almost full ({self.currently_fullness}%). Better clear it")
            except(Full,):
                print("The trash bin is full. Please clear it")
                break
            time.sleep(1)
            print('\n')
        if self.currently_quantity_iter == quantity_iter:
            print("Robot finished to clean")

    def __wash(self):
        self.currently_water -= random.randrange(8, 12, 1)
        if self.currently_water <= 15:
            if self.currently_water <= 0:
                raise WaterZero("The water has run out")
            raise LowWater("The water is almost over")
        print(f'Washes with water level = {self.currently_water}%')

    def __vacuum_cleaner(self):
        self.currently_fullness += random.randrange(5, 9, 1)
        if self.currently_fullness >= 70:
            if self.currently_fullness >= self.max_fullness:
                raise Full("The trash bin is full")
            raise AlmostFull("The trash can is almost full")
        print(f'Cleans with fullness level = {self.currently_fullness}%')


if __name__ == "__main__":
    robot1 = VacuumCleanerRobot(10, 15, 20)
    robot1.move(5)
