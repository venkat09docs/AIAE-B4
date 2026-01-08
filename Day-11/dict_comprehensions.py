# [expression for n in nums if condition]

# SET AND DICTIONARY COMPREHENSIONS

# SET COMPREHENSIONS

names = {'alice', 'BOB', 'charlie', 'DAVE'}

# Convert all names to capitalize first letter, ensuring consistent formatting

cap = { name.capitalize() for name in names }
print(type(cap))
print(cap)

# DICTIONARY COMPREHENSIONS

hyperparams = {'layers': 3, 'units': 256, 'dropout': 0.2}

# Create a new dictionary where all values are doubled -

new_hyperparams = { key: val * 2 for key, val in hyperparams.items() }
print(new_hyperparams)

# Create a set of keys (in uppercase) where values are greater than 0.2

new_dict = {key.upper(): val for key, val in hyperparams.items() if val > 0.2 }
print(new_dict)


years = [2020, 2021, 2022]
dataset_sizes = [10000, 25000, 50000]

# Convert paired elements into dictionary mapping years to dataset sizes
print(dict(zip(years, dataset_sizes)))

sales = {2022: 50000, 2023: 75000, 2024: 100000}

# Calculate profit as 15% of revenue for each year
profit = {year: revenue * (15/100) for year, revenue in sales.items() }
print(profit)

