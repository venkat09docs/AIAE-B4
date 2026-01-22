# File Operations in Python

# Open the file and Read the content
    # Read the content Line by Line

# Open the file and Writing the content
    # Adding Lines (Overriding)
    # Appending New Line

# File Content Type
    # text based file content UTF-8
    # Binary file content (PDF, Image, Audio, Video) (0 / 1)

# Relative Path
file = open("./config/configuration.txt", "rt")
content = file.read()
print(content)

file.close()
print(file.closed)

print("#" * 100)

# Absolute Path

file = open("E:\\AIAE-B4\\Day-16\\config\\configuration.txt", "rt")
content = file.read()
print(content)

file.close()
print(file.closed)

print("#" * 100)

f = open('./config/configuration.txt')
content = f.read(8)
print(content)

content = f.read(4)
print(content)

print(f.tell())

f.seek(50)
print(f.tell())
content = f.read(4)
print(content)
f.close()

print("#" * 100)

with open('./config/configuration.txt', 'r') as file:
    content = file.read()
    print(content)

print(file.closed)

print("#" * 100)

# READING FILES INTO A LIST

with open('./config/configuration.txt') as f:
    content = f.read().splitlines()
    print(content[3])
    print(type(content))

print("#" * 100)

# WRITING TO A FILE

with open('./config/new_config.txt', 'w') as f:
    f.write('This is the 1st Line. \n')
    f.write('This is the 2nd Line. \n')
    f.write('This is the 3rd Line. \n')

with open('./config/new_config.txt', 'at') as f:
    f.write('This is the 4th Line. \n')
    f.write('This is the 5th Line. \n')
    f.write('This is the 6th Line')





