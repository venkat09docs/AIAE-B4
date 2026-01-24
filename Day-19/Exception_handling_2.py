while True:
    try:
        a = int(input("Enter a value: "))
        b = int(input("Enter b Value: "))
        c = a / b
    except ValueError as ve:
        print(f"Value error occurred: {ve}. Please enter valid integers.")
    except ZeroDivisionError as zde:
        print(f"Zero division error occurred: {zde}. 'b' cannot be zero. Please enter a non-zero integer for 'b'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}. Please try again.")
    else:
        print(f"The result of {a} divided by {b} is: {c}")
        break
    finally:
        print("Attempt to perform division operation is complete.")

try:
    age = -2
    if age < 0:
        raise Exception("Age cannot be negative.")
    elif age < 18:
        print("Minor")
    else:
        print("Adult")
except Exception as e:
    print(f"An error occurred: {e}")