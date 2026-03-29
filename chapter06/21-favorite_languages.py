#Looping Through All Values in a Dictionary
#To have unique items, wrap them in a set.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

print('The following languages have been mentioned:')
for language in set(favorite_languages.values()):
    print(language.title())