# FUNCTION ARGUMENTS

# 5 TYPES OF FUNCTION ARGUMENTS:

# 4. USING *args (ARBITRARY POSITIONAL ARGUMENTS)

def calculate_total_cost(base_cost, *items):
    """Calculates the total cost by adding additional variable costs."""
    print(items)
    total_cost = base_cost + sum(items)
    return total_cost

print(calculate_total_cost(5, 2, 3, 7))
print(calculate_total_cost(5))

def create_hashtags(*tags):
    """Creates hashtags based on tags."""
    return ' '.join(tags)

# Example of hashtag creation
print(create_hashtags('#AI', '#Python', '#GenAI', '#LLMs'))

# 5. USING **kwargs (ARBITRARY KEYWORD ARGUMENTS)

def display_user_info(**user_data):
    """Displays user information using keyword arguments."""
    for key, value in user_data.items():
        print(f'{key}: {value}')

# Function call with multiple named arguments
display_user_info(name='Alice', age=30, membership='Premium')
display_user_info(name='Alice', age=30)

