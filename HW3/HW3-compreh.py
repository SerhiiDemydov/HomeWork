# (1)
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)

# Convert (1) to list comprehension
lst = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst)

# (2)
lst_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print(lst_comprehension)

# Convert (2) to regular for with if-else
lst_comprehension = []
for num in range(10):
    if num % 2 == 0:
        lst_comprehension.append(num // 2)
    else:
        lst_comprehension.append(num * 10)
print(lst_comprehension)

# (3)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print(d)

# Convert (3) to dict comprehension
d_dict = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(d_dict)

# (4)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)

# Convert (4) to dict comprehension.
d_dict = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(d_dict)

# (5)
dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(dict_comprehension)

#Convert (5) to regular for with if.
d = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        d[x] = x ** 3
print(d)

# (6)
dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
print(dict_comprehension)

# Convert (6) to regular for with if-else.
d = {}
for x in range (10):
    if x ** 3 % 4 == 0:
        d[x] = x ** 3
    else:
        d[x] = x
print(d)

