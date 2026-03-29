#Looping Through All Key-Value Pairs

user = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key, value in user.items():
    print(f'\nKey: {key}')
    print(f'Value: {value}')