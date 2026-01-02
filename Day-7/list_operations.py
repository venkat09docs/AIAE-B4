# List Operations: Concatenation and Iteration

# -----------------------------
# 1. List Concatenation
# -----------------------------

l1 = [3, 4]
print(l1, id(l1))

l1 = l1 + [5, 6]    # Creates a new list (concatenation)
print(l1, id(l1))   # Memory address changes

l1 += [7, 8]        # Modifies the existing list in place
print(l1, id(l1))   # Memory address remains the same

# extend() adds elements individually
l1.extend([11, 12])
print(l1)
print(len(l1))

# append() vs extend()
l1.append(['a', 'b'])
print(l1)
print(len(l1))

# -----------------------------
# 2. Iteration and Membership Testing
# -----------------------------

ip_list = ['192.168.0.1', '192.168.0.2', '10.0.0.1', '10.0.0.2']

for ip_address in ip_list:
    print(ip_address)

target_ip = ['10.0.0.2', '10.0.0.5']
# Membership testing
for ip_address in target_ip:
    if ip_address in ip_list:
        print(f"{ip_address} found in the list.")
    else:
        print(f"{ip_address} not in the list.")

# 1. Modifying one list affects another if they share the same reference
list_a = [1, 2, 3]
list_b = list_a # list_a references the same object as list_b
print(list_b)

list_b.append(4)
print(list_b, id(list_b))
print(list_a, id(list_a))

# To avoid this, use list.copy() for a shallow copy
list_c = list_a.copy()
print(list_c, id(list_c))

list_c.append(5)
print(list_c, id(list_c))
print(list_a, id(list_a))

list_b.append(6)
print(list_b, id(list_b))
print(list_a, id(list_a))
print(list_c, id(list_c))

nums = [1, 2, 3, 4, 5, 6, 7]
# new_list = []

# for num in nums:
#     if num > 5:
#         new_list.append(num)
#
# print(new_list)

# List comprehension
# [expression for n in nums if condition]
new_list = [num ** 2 for num in nums if num > 5]
print(new_list)