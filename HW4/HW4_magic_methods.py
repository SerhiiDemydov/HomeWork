# 8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
# otherwise return message: "Your city is too small".

class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __new__(cls, name, population):
        instance = super(City, cls).__new__(cls)
        if population < 1500:
            return print('Your city is too small')
        else:
            return instance

# Override a printable string representation of the City class and return: The population of the city {name} is {population}\
    def __str__(self):
        return f'The population of the city {self.name} is {self.population}'


City1 = City('Kyiv', 6000)
print(City1)
City2 = City('Mirnograd', 1000)
print(City2)

# 10*. Override magic method __add__() to perform the additional action as 'multiply' (*) the value which is greater than 10. And perform this add (+) of two instances.

class Count:

    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        if self.count > 10:
            count1 = self.count * 10
        else:
            count1 = self.count
        if other.count > 10:
            count2 = other.count * 10
        else:
            count2 = other.count
        total_count = count1 + count2
        return Count(total_count)

    def __str__(self):
        return f'Count: {self.count}'


c1 = Count(20)
c2 = Count(20)
c3 = c1 + c2
print(c3)

c1 = Count(2)
c2 = Count(2)
c3 = c1 + c2
print(c3)

c1 = Count(20)
c2 = Count(5)
c3 = c1 + c2
print(c3)

# 11. The __call__ method enables Python programmers to write classes where the instances behave like functions and can be called like a function.
# Create a new class with __call__ method and define this call to return sum.
class CallTask:
    def __call__(self, *args, **kwargs):
        return sum(args)


test1 = CallTask()
print(test1(1, 2, 3, 4, 5, 6, 7, 8, 9))

# 12. Making Your Objects Truthy or Falsey Using __bool__().
# Create class MyOrder with cart and customer instance attributes.
# Override the __bool__magic method considered to be truthy if the length of the cart list is non-zero.

class MyOrder:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __bool__(self):
        if len(self.cart) > 0:
            return True
        else:
            return False


My = MyOrder(['a', 'b', 'c'], 'Serhii')
print(bool(My))
You = MyOrder([], 'Andrew')
print(bool(You))
