# CONDITIONAL STATEMENTS (if ... elif ... else)

# if condition1:
#     # True block
#     # Stmt 2
# elif (condition2):
#     # Flase block
#     # Stmt 1
# else if (cond3):
#     # Cond 3 stmts
# else:
#     # else stmts
#     print()

# Syntax reminder:
# if some_condition_is_true:
#     # Code block 1 (executes if the condition is met)
# elif some_other_condition_is_true:
#     # Code block 2 (executes if the first condition is false but this one is met)
# else:
#     # Code block 3 (executes if none of the above conditions are met)

temperature = int(input('Enter the temperature in Celsius: '))

if temperature < 0:
    print("1.It's freezing, wear a heavy coat!")
elif temperature < 15:
    print("2.It's chilly! You might need a jacket!")
elif temperature < 25:
    print("3.The weather is mild. A light sweater should be enough.")
else:
    print("4.It's hot! Stay cool and hydrated.")
    print("5.Outside of if block")

# CONDITIONAL STATEMENTS WITH A STATIC VALUE

temperature = 10

if temperature < 15:
    print("It's chilly! You might need a jacket.")
elif temperature < 27:
    print("The weather is mild. A light sweater should be enough.")
else:
    print("It's hot! Stay cool and hydrated.")
