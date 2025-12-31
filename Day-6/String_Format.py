# STRING CONCATENATION (LESS EFFICIENT)

model_name = 'GPT'
version = 4
msg = 'Hello'

print('Hello from ' + model_name + '-' + str(version) + '!')

# USING F-STRINGS (MORE READABLE & EFFICIENT)
# The f-string automatically converts variables to strings
print(f'{msg}, from {model_name} {version}!')

# FORMATTING NUMBERS WITH F-STRINGS
token_used = 123
cost_per_token = 0.001

# Formatting a floating-point number to 4 decimal places
total_cost = cost_per_token * token_used
print(f'Total cost of tokens: {total_cost}')
