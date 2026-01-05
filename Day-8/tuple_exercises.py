# TUPLE BASICS

# Defining a tuple with geographical coordinates
location = (37.7749, -122.4194)

# Creating empty tuples using two different methods
empty_tuple1 = tuple()
empty_tuple2 = ()

print(location)

# Accessing tuple elements using indexing
print(location[0])
print(location[1])

# location[1] = -1345.14
# print(location[1])

# A single-element tuple requires a trailing comma
number = 10,
print(type(number))

nums = [1, 2, 3, 4, 5]
print(type(nums))
print(type(tuple(nums)))

nums = (1, 2, 3, 4, 5)
print(type(nums))
print(type(list(nums)))

letters = tuple('hello')
print(type(letters))
print(len(letters))
print(letters)

# TUPLE UNPACKING
x, y = 10, 20
# location = (37.7749, -122.4194)
latitude, longitude  = location
print(latitude, longitude)

matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print(matrix[2][1])

numbers = (1, 2, 3, 4, 5)
print(numbers)

for num in numbers:
    print(num)

number = 2
if number in numbers:
    print(f"{number} found in the tuple.")
else:
    print(f"{number} not in the tuple.")

# Slicing Tuple
tuple_data = (1, 2, 3, 4, 5)
print(tuple_data[0:3])
print(tuple_data[::-1])

numbers = (1, 2, 3, 4, 5)
nums_divisible_by_2 = [num for num in numbers if num % 2 == 0]
print(tuple(nums_divisible_by_2))



