from __future__ import annotations
from typing import Dict, Any
import random


class Animal:
    def __init__(self, power: int, speed: int):
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

        # def eat(self, forest: Forest):
        #     pass


class Predator(Animal):

    def eat(self, forest: Forest):
        print('Kus')
        return 2


class Herbivorous(Animal):

    def eat(self, forest: Forest):
        print('gress')
        return 3


AnyAnimal: Any[Herbivorous, Predator]


class Forest:
    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        print('New animal added', animal)

    def remove_animal(self, animal: AnyAnimal):
        pass


def animal_generator():
    while True:
        new_animal = random.choice((Herbivorous(random.randrange(25, 100), random.randrange(25, 100)), Predator(random.randrange(25, 100), random.randrange(25, 100))))
        yield new_animal


animal = {}
if __name__ == "__main__":
    # Create forest
    forest = Forest
    nature = animal_generator()
    # Create few animals
    for i in range(10):
        animal = next(nature)
        print(animal)
        forest.add_animal(animal)

    # Add animals to forest
    # Iterate throw forest and force animals to eat until no predators left
    # animal_generator to create a random animal
    pass
