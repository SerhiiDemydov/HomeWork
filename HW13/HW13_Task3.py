"""
Use Pool.apply() to get the row wise common items in list_a and list_b.
list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]
"""

from multiprocessing import Pool, current_process
import os
import time

list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]


def defined(list1, list2):
    return list(set(list1) & set(list2))


result_pool1 = []
pool = Pool(processes=4)
start_time2 = time.time()
for x in range(4):
    result_pool1.extend(pool.apply(defined, args=(list_a[x], list_b[x])))
print(f'Time work pool.apply 1 = {time.time() - start_time2}')
print(result_pool1)

start_time3 = time.time()
result_pool2 = ([pool.apply(defined, args=(list_a[x], list_b[x])) for x in range(4)])
print(f'Time work pool.apply 2 = {time.time() - start_time3}')
print(result_pool2)
