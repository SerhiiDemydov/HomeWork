# 1. Make the class with composition.
class Laptop:
    def __init__(self):
        self.bat = Battery(80)

    def __str__(self):
        return f'Power energy = {self.bat}%'


class Battery:
    def __init__(self, energy_level):
        self.energy_level = energy_level

    def __str__(self):
        return f'{self.energy_level}'


laptop = Laptop()
print(laptop)


# 2. Make the class with aggregation
class Guitar:
    def __init__(self, string):
        self.string = string


class GuitarString:
    def __init__(self, quantyti_string):
        self.quantyti_string = quantyti_string

    def __str__(self):
        return f'{self.quantyti_string}'


String = GuitarString(7)
guitar = Guitar(String)
print(f'Guitar has {guitar.string} strings')