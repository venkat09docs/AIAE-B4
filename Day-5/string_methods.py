# COMMON STRING METHODS

model_output = 'ai IS the future of everything!'

# STRING CASE CONVERSIONS

# Convert the string to uppercase
print(model_output.upper())
print(model_output.lower())
print(model_output.capitalize())
print(model_output.title())

# STRING STRIPPING

response = ' ?? Hello, human! ?? '

# Remove leading and trailing whitespace characters
print(response.strip())

print(response.strip(' ??'))

text = 'ML is a critical component of modern AI. ML techniques are advancing rapidly.'

# Replace all occurrences of 'ML' with 'Machine Learning'
new_text = text.replace('ML', 'Machine Learning')

print(new_text)
print(text)

# STRING COUNTING
text = 'AI is the FUture. Embrace the future of AI!'
print(text.lower().count('future'))

# STRING SPLITTING
statement = 'AI breakthrough, at every step'
words = statement.split(' ')
print(words)
print(type(words))

# STRING JOINING
terms = ['AI', 'ML', 'GenAI', 'LLM', 'NLP']
print(type(terms))

# Join the list elements into a single string, separated by ', '
ml_words = ', '.join(terms)
print(type(ml_words))

# Remove 'https://' from the beginning of the URL
url = 'https://example.com'

domain_url = url.removeprefix('https://')
print(domain_url)

# Remove '.pdf' from the end of the filename
filename = 'state_of_ai_2025.pdf'
clean_name = filename.removesuffix('.pdf')
print(clean_name)

