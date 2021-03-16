from __future__ import annotations
from typing import Dict, Any
from abc import ABC, abstractmethod
import random
import uuid
import time


class Animal(ABC):
    def __init__(self, power: int, speed: int):
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self, forest: Forest):
        pass


class Predator(Animal):

    def eat(self, forest: Forest):
        victim = random.choice(list(forest.animals.values()))
        if victim.id == self.id:
            print('Predator did not find anyone')
        else:
            print(
                f'{__class__.__name__} {self.id} hunts with {self.current_power} power and {self.speed} speed an animal {victim.id} {victim.__class__.__name__} with {victim.current_power} power and {victim.speed} speed')
            if self.speed > victim.speed:
                print('Predator caught up with the victim')
                if self.current_power > victim.current_power:
                    print('Predator win in attack')

                    # Victim's power after attack
                    successful_attack(self, victim)

                    # Predator's power after successful attack
                    recovery_power(self)

                else:
                    print('Predator dont win in attack')

                    # Predator's power after victim ran away
                    unsuccessful_attack(self)

                    # Victim's power after victim ran away
                    unsuccessful_attack(victim)

            else:
                print(f'The victim ran away')

                # Predator's power after victim ran away
                unsuccessful_chase(self)

                # Victim's power after victim ran away
                unsuccessful_chase(victim)


class Herbivorous(Animal):

    def eat(self, forest: Forest):
        recovery_power(self)


def recovery_power(animal: AnyAnimal):
    print(f'{animal.__class__.__name__} is eating with {animal.current_power} power')
    if animal.current_power + animal.max_power * 0.5 >= animal.max_power:
        animal.current_power = animal.max_power
    else:
        animal.current_power = round(animal.current_power + animal.max_power * 0.5, 1)
    print(
        f'{animal.__class__.__name__} {animal.id} finished to eat with {animal.current_power} power')


def unsuccessful_attack(animal: AnyAnimal):
    if animal.current_power - animal.max_power * 0.3 <= 0:
        forest.remove_animal(animal)
        print(f'{animal.__class__.__name__} {animal.id} die')
    else:
        animal.current_power = round(animal.current_power - animal.max_power * 0.3, 1)
        print(
            f'{animal.__class__.__name__} {animal.id} power after unsuccessful attack is {animal.current_power}')


def successful_attack(predator: AnyAnimal, herbivorous: AnyAnimal):
    if herbivorous.current_power - predator.current_power <= 0:
        forest.remove_animal(herbivorous)
        print(f'{herbivorous.__class__.__name__} {herbivorous.id} die')
    else:
        herbivorous.current_power -= predator.current_power
        print(f'{herbivorous.__class__.__name__} {herbivorous.id} alive with {herbivorous.current_power}')


def unsuccessful_chase(animal: AnyAnimal):
    if animal.current_power - animal.max_power * 0.3 <= 0:
        forest.remove_animal(animal)
        print(f'{animal.__class__.__name__} {animal.id} die')
    else:
        animal.current_power = round(animal.current_power - animal.max_power * 0.3, 1)
        print(
            f'{animal.__class__.__name__} {animal.id} power after unsuccessful chase is {animal.current_power}')


AnyAnimal: Any[Herbivorous, Predator]


class Forest:
    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        print('New animal added', animal)
        self.animals.update({animal.id: animal})

    def remove_animal(self, animal: AnyAnimal):
        print(f'{animal.id} animal removed')
        self.animals.pop(animal.id)

    def any_predator_left(self):
        for x in list(self.animals.values()):
            if x.__class__.__name__ == 'Predator':
                print(f'{x.__class__.__name__} is in forest')
                if len(list(self.animals.values())) == 1:
                    print(f'Only 1 {x.__class__.__name__} live in forest')
                    return False
                return True
        print(f'Only {x.__class__.__name__} live in forest')
        return False


def animal_generator():
    while True:
        new_animal = random.choice((Herbivorous(random.randrange(25, 100, 1), random.randrange(25, 100, 1)),
                                    Predator(random.randrange(25, 100, 1), random.randrange(25, 100, 1))))
        new_animal.id = uuid.uuid4()
        yield new_animal


if __name__ == "__main__":
    # Create forest
    forest = Forest()
    nature = animal_generator()
    # Create few animals
    for i in range(10):
        animal = next(nature)
        print(animal.__dict__)
        # Add animals to forest
        forest.add_animal(animal)
    print([{x.__class__.__name__: x.__dict__} for x in list(forest.animals.values())])
    # Iterate throw forest and force animals to eat until no predators left
    while True:
        if not forest.any_predator_left():
            break
        random.choice(list(forest.animals.values())).eat(forest)
        print([{x.__class__.__name__: x.__dict__} for x in list(forest.animals.values())])
        time.sleep(1)
