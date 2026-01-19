# LAMBDA EXPRESSIONS

# Regular function equivalent

def add(a, b, c):
    """Returns the sum of three numbers."""
    return a + b + c

print(add(2,3,4))

# Syntax:
# lambda parameters: expression

print((lambda a, b, c: a + b + c)(2,3,4))

square = lambda x = 10: x ** 2
print(square(100))

friends = [('Diana Y', 30), ('Ana', 25), ('Tudor', 22)]

friends.sort(key=lambda person: person[1])
print(friends)

friends.sort(key=lambda person: len(person[0]), reverse=True)
print(friends)


