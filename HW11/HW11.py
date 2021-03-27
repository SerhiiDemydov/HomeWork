from functools import wraps

# 1. double_result
# This decorator function should return the result of another function multiplied by two
print("------------------------ Task 1 ------------------------")


def double_result(func):
    @wraps(func)
    def inner(a, b):
        return func(a, b) * 2

    return inner


def add(a, b):
    return a + b


print(f'Function add (5,5) = {add(5, 5)}')  # 10


@double_result
def add(a, b):
    return a + b


print(f'Function add (5,5) with decorator multiplied by two = {add(5, 5)}')  # 20

# 2. only_odd_parameters
# This decorator function should only allow a function to have odd numbers as parameters,
# otherwise return the string "Please use only odd numbers!"
print("------------------------ Task 2 ------------------------")


def only_odd_parameters(func):
    @wraps(func)
    def inner(*args, **kwargs):
        for x in args:
            if x % 2 == 0:
                return print("Please use only odd numbers!")
        return func(*args, **kwargs)

    return inner


@only_odd_parameters
def add(a, b):
    return print(f'Function add ({a}, {b}) = {a + b}')


add(5, 5)  # 10
add(4, 4)  # "Please use only odd numbers!"


@only_odd_parameters
def multiply(a, b, c, d, e):
    return print(f'Function multiply({a}, {b}, {c}, {d}, {e}) {a * b * c * d * e}')


multiply(1, 3, 5, 7, 9)  # 945
multiply(1, 2, 3, 4, 5)  # "Please use only odd numbers!"

# 3.* logged
# Write a decorator which wraps functions to log function arguments and the return value on each call.
# Provide support for both positional and named arguments (your wrapper function should take both *args
# and **kwargs and print them both):
print("------------------------ Task 3 ------------------------")


def logged(funct):
    @wraps(funct)
    def wrapper(*args, **kwargs):
        """
        logged
        :param args:
        :param kwargs:
        :return: fun(*args, **kwargs)
        """
        print("You called {}{}{}".format(funct.__name__, args, kwargs))
        return funct(*args, **kwargs)

    # log function arguments and its return value
    return wrapper


@logged
def func(*args):
    """
    func
    :param args:
    :return: 3 + len(args)
    """
    print(f'It returned {3 + len(args)}')
    return 3 + len(args)


print(func.__name__)
print(func.__doc__)
func(4, 4, 4)

# you called func(4, 4, 4)
# it returned 6


# 4. type_check
# you should be able to pass 1 argument to decorator - type.
# decorator should check if the input to the function is correct based on type.
# If it is wrong, it should print(f"Wrong Type: {type}"), otherwise function should be executed.
print("------------------------ Task 4 ------------------------")


def type_check(correct_type):
    def check(func):
        @wraps(func)
        def inner(a):
            if isinstance(a, correct_type):
                return func(a)
            return print(f'Wrong type: "{type(a).__name__}", should be "{correct_type.__name__}"')

        return inner

    return check


@type_check(int)
def times2(num):
    """
    Function ""times2
    :param num:
    :return: num * 2
    """
    return num * 2


print(times2.__doc__)
print(times2(2)) # 4
times2('Not A Number')  # "Wrong Type: string" should be printed, since non-int passed to decorated function


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World')) # H
first_letter(['Not', 'A', 'String'])  # "Wrong Type: list" should be printed, since non-str passed to decorated function
