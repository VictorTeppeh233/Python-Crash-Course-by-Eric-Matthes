# assignment 8.11

# Initial list of messages and empty list to store sent messages
short_messages = [
    'I love Ghana.',
    'Ghana is in West Africa.',
    'Accra is the capital of Ghana.',
    'Ghana has 16 Regions.'
]
sent_messages = []

# Creating the function
def send_messages(messages):
    """Simulate sending each message and move it to sent_messages."""
    while messages:
        current_message = messages.pop()
        sent_messages.append(current_message)
        print(f'Sending message: {current_message}')

# Calling the function with a copy of the list
send_messages(short_messages[:])  # [:] creates a copy

# Printing the lists
print('Original messages list:')
print(short_messages)
print('-' * 30)
print('Sent messages list:')
print(sent_messages)