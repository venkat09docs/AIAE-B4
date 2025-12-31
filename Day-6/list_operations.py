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