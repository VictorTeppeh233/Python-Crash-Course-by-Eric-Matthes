# Assignment 6.1

persons = {
    'first_name': 'albert',
    'last_name': 'einstein',
    'age': '98',
    'city': 'princeton',
}

full_name = f"{persons['first_name'] } {persons['last_name'] }"
print(f'His name is {full_name.title()}. He is {persons["age"]} years old, and lives at {persons['city'].title()}.')