lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

# Sort lst_to_sort from min to max
print(sorted(lst_to_sort))
lst_to_sort.sort()
print(lst_to_sort)

# Sort lst_to_sort from max to min
print(sorted(lst_to_sort, reverse=True))
lst_to_sort.sort(reverse=True)
print(lst_to_sort)


lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

# Use map and lambda to update the lst_to_sort by multiply each element by 2
print(list(map(lambda x: x * 2, lst_to_sort)))


# Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]
list_A_new1 = []

for x in range(len(list_A)):
    list_A_new1.append(list_A[x] + (list_B[x] - list_A[x]))
print(list_A_new1)

list_A_new2 = [list_A[x] + (list_B[x] - list_A[x]) for x in range(len(list_A)) ]
print(list_A_new2)

# Use reduce and lambda to compute the numbers of a lst_to_sort.
from functools import reduce
print(f"lst_to_sort = {lst_to_sort}")
print(reduce(lambda x, y: x + y, lst_to_sort))

# Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
print(list(filter(lambda x: x % 2 == 1, lst_to_sort)))

# Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
b = range(-10, 10)
print(list(filter(lambda x: x < 0 , b)))

# Using the filter function, find the values that are common to the two lists:
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
print(list(filter(lambda x: x in list_1, list_2)))
