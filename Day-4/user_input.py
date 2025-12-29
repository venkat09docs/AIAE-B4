# GETTING USER INPUT

# BASIC USER INPUT
# Prompt the user to ask a question
# name = input('Enter Your Name:')
# print(name)
#
# age = input('Enter Your Age:')
# print(name + ' is ' + age + ' years old.')

training_hours = int(input('Enter hours spent training the model: '))
print(type(training_hours))

iterations = int(input('Enter the number of model iterations (integer): '))
datasets = int(input('Enter the number of datasets: '))

total = iterations * datasets
print(total)



