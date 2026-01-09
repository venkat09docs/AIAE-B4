# Types of loops:

# 1. For loops - iterate over sequences (lists, tuples, strings, dictionaries, etc.)
#for n in nums

# 2. While loops - execute as long as a condition is True

numbers = [1, 2, 3, 4, 5]

for no in numbers:
    print(f"Number - {no}")

tweets = [
    'Exploring AI applications',
    'Machine Learning is the future',
    'Having lunch with friends',
    'New advances in GenAI'
]

for tweet in tweets:
    if 'AI' in tweet or 'Machine Learning' in tweet:
        print(f"Filtered Tweet - {tweet}")

feedback = [
    'Great service!',
    'Excellent response time',
    'Had to wait too long',
    'Excellent support from staff'
]

for comment in feedback:
    if 'excellent' in comment.lower():  # Convert to lowercase for case-insensitive search
        print(f'Highlighted Feedback: {comment}')

temperature_readings = [71, 74, 78, 82, 85, 90]
threshold = 80

for temp in temperature_readings:
    if temp > threshold:
        print(f'Warning: Temperature exceeded safe limit at {temp}°F')
