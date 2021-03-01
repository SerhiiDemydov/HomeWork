# 1. Create a Vehicle class with max_speed and mileage instance attributes
class Venicle:
    def __init__(self, max_speed, mile):
        self.max_speed = max_speed
        self.mile = mile

# 2. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class and will have seating_capacity own method
class Bus(Venicle):
    def __init__(self, max_speed, mile, seating_capacity):
        self.seating_capacity = seating_capacity
        self.max_speed = max_speed
        self.mile = mile
        super().__init__(max_speed, mile)

    def bus_capacity(self):
        print(f'Capacity in bus = {self.seating_capacity}')


# 3. Determine which class a given Bus object belongs to (Check type of an object)
School_bus = Bus(30, 100, 36)
print(type(School_bus.max_speed))
print(type(School_bus.mile))
print(type(School_bus))
School_bus.bus_capacity()
print(issubclass(Bus, Venicle))

# 4. Determine if School_bus is also an instance of the Vehicle class
print(f'School_bus is an instance of Vehicle class - {isinstance(School_bus,Venicle)}')

# 5. Create a new class School with get_school_id and number_of_students instance attributes
class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

#6*. Create a new class SchoolBus that will inherit all of the methods from School and Bus and will have its own - bus_school_color
class SchoolBus(School,Bus):
    def __init__(self, get_school_id, number_of_students, max_speed, mile,  seating_capacity, bus_school_color):
        School.__init__(self, get_school_id, number_of_students)
        Bus.__init__(self, max_speed, mile, seating_capacity)
        self.bus_school_color = bus_school_color


Bus_number1 = SchoolBus(1235, 200, 90, 240, 35, 'yellow')
print(f'School number {Bus_number1.get_school_id} has {Bus_number1.bus_school_color} bus.')



