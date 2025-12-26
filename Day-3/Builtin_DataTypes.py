# PYTHON'S BUILT-IN DATA TYPES

# 1. Numbers: int and float

age = 25 # Integer Data Type
temparature = 20.1 # float type

# 8 bits = 1 byte

# Static vs. Dynamic Typing
# Java (example - for comparison)
# int age;
# age = 40

# 2. Booleans: Logical values => True or False

print(age == 40)
print(age < 30)

# 3. Strings: Ordered sequences of characters, stored in UTF-8 encoding.

model_name = "Gemini" # "" / ''
print(len(model_name))

# 4. List: Ordered, mutable sequences of objects.
person = ["RNS", 13, False, "Rise n Shine", 13]
print(person)

# 5. Tuple: Ordered, immutable sequences of objects.
coordinates = (40.3, 54.7)

# 6. Sets: Mutable collections of unordered, unique objects.
ip_addresses = {'100.0.0.1', '80.1.1.2', '5.6.1.4', '5.6.1.4'}
print(type(ip_addresses))
print(ip_addresses)

# 7. Dictionary: Collections of unordered key-value pairs
employee = {"name": "RNS", "age": 13, "is_permanent": False}
print(type(employee))


