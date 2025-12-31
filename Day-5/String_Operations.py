# CORE STRING OPERATIONS: INDEXING, SLICING, CONCATENATING

# Index based access
# Ordered collection of characters starts from 1 ends at n
# 0-based indexing and ends at n-1
message = 'GenAI is amazing!'

# INDEXING: Accessing individual characters in a string
print(message[4])
print(message[9])
print(len(message))
print(message[16])
print(message[-1])
print(message[-2])

# STRINGS ARE IMMUTABLE
# message[0] = 'X'

# STRING CONCATENATION
greeting = 'Hello, '
role = 'AI enthusiast'

full_greeting = greeting + role + '!'
print(full_greeting)

print('Version ' + str(1.0) )

# STRING REPETITION

# * in integer 3 * 4 = 12

# Repeating a string multiple times
separator = '??'
print(separator * 100)

tech = 'Machine Learning'

# string[start_index:stop_position]

print(tech[0:7])
print(tech[8:16])
print(tech[:7])

print(tech[-8:])

# string[start_index:stop_position:step]
print(tech[0::3])

print(tech[::-1])




