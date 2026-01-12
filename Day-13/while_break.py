# THE break STATEMENT

keywords = ['innovation', 'deep learning', 'AI revolution', 'neural networks', 'machine learning']

if 'AI revolution' in keywords:
    print("Keyword found")


for word in keywords:
    print(f'Checking word: {word}')
    if word == 'AI revolution':
        print('Urgent keyword found! Stopping search.')
        break # Exits the loop as soon as 'AI revolution' is found


temperature = 70

while temperature < 80:
    print(f'The current temperature is {temperature}°F.')

    if temperature == 75:
        print('Temperature threshold reached. Stopping monitoring.')
        break  # Exits the loop once temperature reaches 75

    temperature += 1
else:
    print('Temperature monitoring complete. System stable.')


for i in range(3):
    for j in range(3):
        if j == 1:
            break
print(f'i={i}, j={j}')