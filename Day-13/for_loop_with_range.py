# Iteration
    # Start Position (Index 0)
    # Condition
    # Step/Increment / decrement

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# len = len(numbers)

# Working with Ranges in Python

# -----------------------------
# 1. Using range() in a Loop
# -----------------------------

# range(start, stop) -> stop is exclusive
for i in range(5):  # 0 to 4
    print(f"Index: {i}")

for participant in range(1, 101):
    print(f"Participant: {participant}")

# -----------------------------
# 2. Creating a List from a Range
# -----------------------------

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = list(range(1, 11))  # Creating a list of numbers from 1 to 10
print(type(numbers))
print(numbers)

# [start:stop:step]
even_numbers = range(0, 11, 2)  # Creating a range of even numbers from 1 to 10
print(type(even_numbers))
print(list(even_numbers))

# -----------------------------
# 3. Looping a Fixed Number of Times (Ignoring Index)
# -----------------------------
for _ in range(5):  # The underscore (_) is a convention for an unused variable
    print("Analyzing Data")