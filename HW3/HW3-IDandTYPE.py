int_a = 55
str_b = 'cursor'
set_c = {1,2,3}
lst_d = [1,2,3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

# Define the id of next variables:
print(id(int_a))
print(id(str_b))
print(id(set_c))
print(id(lst_d))
print(id(dict_e))

# Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append(4)
lst_d.append(5)
print(lst_d)
print(id(lst_d))

lst_d.extend([6, 7])
print(lst_d)
print(id(lst_d))

# Define the type of each object from step 1.
print(type(int_a))
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))

#Check the type of the objects by using isinstance.
print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, list))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))

