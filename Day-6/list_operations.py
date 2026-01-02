# ESSENTIAL LIST METHODS IN PYTHON

# ADDING ELEMENTS TO A LIST

list1 = list()
# append(): Adds a single element to the end of the list
list1 = [1, 2.2, 'abc']
list1.append([4, 5])
print(list1)

# extend(): Extends the list with elements from an iterable
list1.extend(['x', 'y', 'z'])
print(len(list1))

# insert(): Inserts an element at a specific index
list1.insert(3, False)
print(len(list1))
print(list1)

list1[3] = True
print(list1)

# REMOVING ELEMENTS FROM A LIST
# clear(): Removes all elements from the list
list1.clear()
print(len(list1))

# pop(): Removes and returns an element by index (default is the last element)
l2 = [10, 20, 30, 40]
l2.pop()
print(l2)

l2.pop(1)
print(l2)

# str[start_index:stop_position:step]

numbers = [1, 2, 3, 4, 5]

# Output: [2, 3, 4]
print(numbers[1:4])

# Output: [1, 2, 3]
print(numbers[0:3])

# Output: [3, 4, 5]
print(numbers[2:5])

# Output: [2, 4]
print(numbers[1:5:2])

# Output: [5, 4, 3, 2, 1]
print(numbers[::-1])

# REVERSING AND SORTING LISTS
# reverse(): Reverses the order of elements in place
sequence = [1, 2, 3, 4]
sequence.reverse()
print(sequence)

# sort(): Sorts the list in ascending order (default)
numbers = [3, 1, 4, 1, 5]
numbers.sort()
print(numbers)

# Descending Order
numbers = [3, 1, 4, 1, 5]
numbers.sort(reverse=True)
print(numbers)

# sorted(): Returns a new sorted list without modifying the original
numbers = [3, 1, 4, 1, 5]
sorted_numbers = sorted(numbers)  # Creates a new sorted list
print(sorted_numbers)
print(numbers)

# append
# extend
# insert
# clear
# pop
# reverse
# sort
# sorted
# numbers[index]
# numbers[index] = value
# numbers[start:stop:step]