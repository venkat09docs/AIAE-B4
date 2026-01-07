# DICTIONARY OPERATIONS AND METHODS: ACCESSING, UPDATING, .GET(), .KEYS(), AND .VALUES()

# ASSIGNMENT AND COPYING

# Creating a dictionary
model_params = {'layers': 24, 'units': 512, 'activation': 'relu'}

shared_params = model_params
print(shared_params)
print(model_params)

model_params['units'] = 1024
print(shared_params)
print(model_params)

shared_params['layers'] = 48
print(shared_params)
print(model_params)

safe_params = model_params.copy()
print(model_params)
print(safe_params)

model_params.clear()
print(model_params)
print(safe_params)

# MERGING DICTIONARIES using update() method

base_config = {'batch_size': 32, 'epochs': 10}
version_config = {'learning_rate': 0.001, 'units': 128, 'epochs': 20}

base_config.update(version_config)
print(base_config)
print(len(base_config))

# Get all keys from base_config
print(base_config.keys())

# Get all values from base_config
print(base_config.values())

print(base_config.items())

# ITERATING OVER KEYS, VALUES, AND ITEMS

for key in base_config.keys():
    print(f'key => {key}')

for val in base_config.values():
    print(f'Value => {val}')

for dict_key, dict_val in base_config.items():
    print(f'{dict_key} => {dict_val}')

# TESTING MEMBERSHIP USING in

print('batch_size' in base_config.keys())
print(32 in base_config.values())
print(('batch_size', 32) in base_config.items())


# Logical AND, logical OR

# cond_1  AND cond_2  =  Result
#   T     AND   F   =     F
#   F     AND   T   =     F
#   F     AND   F   =     F
#   T     AND   T   =     T

# cond_1  OR cond_2  =  Result
#   T     OR   F   =      T
#   F     OR   T   =      T
#   T     OR   T   =      T
#   F     OR   F   =      F

# Find common keys between two dictionaries using set intersection
config_a = {'batch_size': 32, 'optimizer': 'adam'}
config_b = {'batch_size': 64, 'optimizer': 'adam', 'momentum': 0.9}

common_keys = config_a.keys() & config_b.keys()
print(common_keys)

merged_dict = config_a | config_b
print(merged_dict)

# CLEARING A DICTIONARY

merged_dict.clear()
print(merged_dict)

data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
age = data.pop('age', 'Not found')
print(age)
print(data)

last_item = data.popitem()
print(last_item)
print(data)

del data['name']
print(data)




