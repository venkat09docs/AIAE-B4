# Python Errors and Exception Handling

# Types of Exceptions:
# 1. Syntax Errors # IDE helping
# 2. Runtime Errors

def loop_to_print_upto_ten():
    for x in range(10):
        print(x)

print(loop_to_print_upto_ten)
# print(x)

# a, b = 10, 0
# c = a / b
# print(c)

with open('a.txt', 'r') as file:
    content = file.read()
    print(content)

# Exception Handling using try, except, finally, else

try:
    file = open('a.txt', 'r')
    content = file.read()
    print(content)

    a, b = 10, 2
    c = a / b
    print(c)
except FileNotFoundError as fnf_error:
    print(f"File not found error occurred: {fnf_error}")
except ZeroDivisionError as zero_division_error:
    print(f"Zero division error occurred: {zero_division_error}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("No exceptions occurred. Execution successful.")
finally:
    print("Execution of try-except block is complete.")
    print(file.closed)
    if file.closed:
        print("File is properly closed.")
    else:
        print("File is not properly closed.")
        file.close()




