# Key Python Operators: Assignment, Comparison, and Identity Operators

# Assignment Operator
a = 5

a = a + 2
print(a)

# Augmented Assignment Operators
a += 2 # Equivalent to: a = a + 2
print(a)

a -= 4 # Equivalent to: a = a - 4
print(a)

a *= 10 # Equivalent to: a = a * 10
print(a)

# Incrementing and decrementing
a += 1 # Equivalent to: a = a + 1
a -= 1  # Equivalent to: a = a - 1

a, b = 10, 5
print(a == b)
print(a > b)

a = 2
print(id(a)) # Prints the memory address of a

a = 3 # Modifies the value of a
print(id(a)) # Memory address changes since integers are immutable

numbers = [1, 2, 3]
print(numbers)
print(id(numbers))

numbers.append(10)
print(numbers)
print(id(numbers))



