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
    max_battery = 100  # %
    max_fullness = 100  # %
    max_water = 100  # %

    def __init__(self):
        self.currently_battery = self.max_battery
        self.currently_fullness = 0
        self.currently_water = self.max_water

    def move(self):
        print(f'Robot starts to move with level battery = {self.currently_battery}%')
        print(f'Robot starts to wash with water level = {self.currently_water}%')
        print(f'Robot starts to clean with fullness level = {self.currently_fullness}%\n\n')

        while True:

            try:
                self.currently_battery -= random.randrange(3, 11, 1)
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

    def __wash(self):
        self.currently_water -= random.randrange(8, 12, 1)
        if self.currently_water <= 15:
            if self.currently_water <= 0:
                raise WaterZero("The water has run out")
            raise LowWater("")
        print(f'Washes with water level = {self.currently_water}%')

    def __vacuum_cleaner(self):
        self.currently_fullness += random.randrange(5, 9, 1)
        if self.currently_fullness >= 70:
            if self.currently_fullness >= 98:
                raise Full("The trash bin is full")
            raise AlmostFull("The water is almost over")
        print(f'Cleans with fullness level = {self.currently_fullness}%')


if __name__ == "__main__":
    robot1 = VacuumCleanerRobot()
    robot1.move()
