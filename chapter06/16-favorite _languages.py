# Looping Through All the Keys in a Dictionary

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

for name in favorite_languages.keys():
    print(name.title())

print()

for name in favorite_languages:
    print(name.title())