"""
4. Divide the work between 2 methods: print_cube that returns the cube of number
and print_square that returns the square of number. These two methods should be executed by using 2 different processes.
"""
from multiprocessing import Process, current_process, cpu_count
from concurrent.futures import ProcessPoolExecutor
import os


def print_cube(a):
    print(f"Process with id:{os.getpid()} and name {current_process().name} started")
    return print(f'The cube of Number {a} = {a ** 3}')


def print_square(b):
    print(f"Process with id:{os.getpid()} and name: {current_process().name} started")
    return print(f'The square of Number {b} = {b ** 2}')


print(f'Your count CPU: {cpu_count()}')

with ProcessPoolExecutor(max_workers=2) as pool:
    pool.submit(print_cube, 4)
    pool.submit(print_square, 6)

p1 = Process(name="print_cube", target=print_cube, args=(4,))
p2 = Process(name="print_square", target=print_square, args=(6,))
p1.start()
p2.start()