#With .format and curly braces {}
print("Anna has {} apples and {} peaches.".format(6, 2))

#By passing index numbers into the curly braces.
print("Anna has {1} apples and {0} peaches.".format(6, 2))

#By using keyword arguments into the curly braces.
print("Anna has {apple} apples and {peache} peaches.".format(apple=6, peache=2))

#8*. With indicators of field size (5 chars for the first and 3 for the second)
print("Anna has {0:5} apples and {1:3} peaches.".format(6, 2))

#With f-strings and variables
a = 6
b = 3
print(f"Anna has {b} apples and {a} peaches.")

#10. With % operator
a = 6
b = 3
c = "small"
print("Anna has %d apples and %d %s peaches." % (a, b, c))

#With variable substitutions by name (hint: by using dict)
a = 3
b = 6
c_dict = {"peaches": b, "apples": a}
print("Anna has %(apples)d apples and %(peaches)d peaches." % c_dict)