# Smart looping techniques: continue, pass, break

sentence = 'AI is the future of technology.'

# the, in , of

for word in sentence.split():
    # print(word)
    if word.lower() in ['the', 'in', 'of']:
        continue
    print(f"Important Word: {word}")

while True:
    prompt = input("Enter a prompt for the model: ")
    if len(prompt) < 5:
        print("Prompt too short, please provide more details.")
        continue
    print(f"Generating response for: {prompt}")
    break


# pass - A null operation.
# It is used when a statement is required syntactically, but you do not want to execute any commands or code.
# It's often used as a placeholder.

for model in range(5):
    pass