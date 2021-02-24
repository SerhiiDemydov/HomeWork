# (7)
def foo(x, y):
    if x < y:
        return x
    else:
        return y

print(foo(1, 2))

# Convert (7) to lambda function
foo = lambda x, y: x if x < y else y
print(foo(1, 2))


# (8)
foo = lambda x, y, z: z if y < x and x > z else y
print(foo(1, 2, 3))

# Convert (8) to regular function
def foo(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y
print(foo(1, 2, 3))


