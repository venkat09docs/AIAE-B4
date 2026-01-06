# Sets basics

# mutable, un-ordered, no duplicates
# {}

unique_ids = {1, 2, 3, 3, 'a', 'b', 4}

print(unique_ids)
print(len(unique_ids))

# empty_set = {} # this creates an empty dictionary, not a set
# print(type(empty_set))

empty_set2 = set()
print(type(empty_set2))

sentences = ['Hello world', 'AI is amazing', 'Hello world', 'Python is great']
print(type(sentences))
unique_sentences = set(sentences)
print(list(unique_sentences))

#unique_ids = {1, 2, 3, 3, 'a', 'b', 4}
# Adding elements to a set
unique_ids.add(5)
print(unique_ids)

unique_ids.remove(2)
print(unique_ids)

unique_ids.remove(3)
print(unique_ids)

# unique_ids[3] = 10

unique_ids.update(['a1','b1','c1'])
print(unique_ids)

immutable_element = tuple([4, 5, 6])
print(type(immutable_element))
print(immutable_element)
unique_ids.add(immutable_element)
print(unique_ids)

for uid in unique_ids:
    print(uid)

if 2 in unique_ids:
    print("2 is present in the set.")
else:
    print("2 is not present in the set.")

# immutable, unique values, un-ordered collection
frozen_set_example = frozenset([1, 2, 3, 4, 4, 5])
print(frozen_set_example)
print(type(frozen_set_example))

# frozen_set_example.add(6)
# print(frozen_set_example)