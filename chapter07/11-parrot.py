# Using a Flag

prompt = "Tell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. \n"

active = True
while active:
    message = input(prompt)
    print("-" * 20)

    if message == "quit":
        active = False
    else:
        print(message)
    