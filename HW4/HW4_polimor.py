# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method. Create two instances, one of Bear and one of Wolf,
# make a tuple of it and by using for call their action using the same method.
class Bear:
    def make_sound(self):
        print('Bear')


class Wolf:
    def make_sound(self):
        print('Wolf')


bear = Bear()
wolf = Wolf()

for animals in (bear, wolf):
    animals.make_sound()
