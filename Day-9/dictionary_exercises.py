# DICTIONARY BASICS

# Creating a dictionary with various key types

model_config = {
    'model_name': 'GPT',
    'layers': 96,
    'parameters': '200B',
    (1,2): 0.7,
    True: 'active',
    10: 'Ten'
    # [1,2,3]: 'list_key'  # This will raise a TypeError
}
print(model_config)
print(type(model_config))
print(len(model_config))

hyperparameters = {
    'learning_rate': 0.0001,
    'dropout_rate': 0.3,
    'optimizer': 'Adam'
}

print(hyperparameters)

# Accessing dictionary values using keys
print(hyperparameters['optimizer'])
print(hyperparameters['dropout_rate'])

print(hyperparameters.get('learning_rate', 'Key not Found'))

hyperparameters['dropout_rate'] = 0.2
print(hyperparameters)

hyperparameters['batch_size'] = 64
print(hyperparameters)

hyperparameters['batch_size'] = 78
print(hyperparameters)

# BEST PRACTICES FOR DICTIONARIES

# 1. Stick to **immutable keys** (e.g., strings, numbers, tuples)
# 2. Avoid **duplicate keys** (last assigned value will override)
# 3. Use **.get()** for safe access to prevent errors


