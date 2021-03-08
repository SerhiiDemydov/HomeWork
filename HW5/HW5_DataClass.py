# 6.
import dataclasses


@dataclasses.dataclass
class AddressBookDataClass:
    """
    Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)
    """
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


My = AddressBookDataClass(1, 'Serhii', '0994354345', 'Kosoha 90', 'safsaf@fsagfa.com', '24.04.95', 25)
print(f'My = {My}')

# 7. Create the same class (6) but using NamedTuple
import collections

AddressBookDataClass = collections.namedtuple('AddressBookDataClass',
                                              ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])

My2 = AddressBookDataClass(1, 'Serhii', '0994354345', 'Kosoha 90', 'safsaf@fsagfa.com', '24.04.95', 25)
print(f'My2 = {My2}')


# 8.
class AddressBook:
    """
    Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
    Make its str() representation the same as for AddressBookDataClass defined above.
    """

    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f'{self.__class__.__name__}(key={self.key}, name={self.name}, phone_number={self.phone_number}, address={self.address}, email={self.email}, birthday={self.birthday}, age={self.age})'


My3 = AddressBook(1, 'Serhii', '0994354345', 'Kosoha 90', 'safsaf@fsagfa.com', '24.04.95', 25)
print(f'My3 = {My3}')


# 9.
class Person:
    """
    Change the value of the age property of the person object
    """
    name = "John"
    age = 36
    country = "USA"


person = Person()
person.age = 20
print(person.age)


# 10.
class Student:
    """
    Add an 'email' attribute of the object student and set its value
    Assign the new attribute to 'student_email' variable and print it by using getattr
    """
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name


student = Student(1, "Jon")
student.email = 'fsadfg32@gmail.com'
print(getattr(student, 'email'))
student_email = 'asdgasdf@gmail.com'
student_email = getattr(student, 'email')
# setattr(student, 'student_email', "asdgasdf@gmail.com")
print(student_email)


# 11*.
class Celsius:
    """
    By using @property convert the celsius to fahrenheit
    Hint: (temperature * 1.8) + 32)
    """

    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return (self._temperature * 1.8) + 32


# create an object
temp = Celsius(23)

print(f'Temperature = {temp.temperature} F')
