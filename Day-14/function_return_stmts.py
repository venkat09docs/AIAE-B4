# THE return STATEMENT

# The `len()` function returns the length of a string
name = " RNS Tech"
length = len(name)
print(length)

# RETURNING VALUES FROM FUNCTIONS

def add(a,b):
    """Returns the sum of two numbers."""
    return a + b

sum = add(100,200)
print(add(20, 30))
print(sum)

# A function with no return statement
def func():
    """ Placeholder function, does nothing"""
    pass

def example_function():
    return '1.This is the return value!'
    print("This line will never execute")

result = example_function()
print(result)  # Output: This is the return value!

def myfunc(x=10):
    """Returns multiple values: the input number, its square, and its cube."""
    return x, x ** 2, x ** 3, x ** 4

a, b, c, d = myfunc(x=20)
print(f'a= {a}, b= {b}, c= {c}, d= {d}')  # Output: a=10, b=100, c=1000, d=10000