myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'lazy'}
print(myCat['size'])

# direct comparison of dictionaries
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(eggs == ham)
print(eggs.values())
print(eggs.keys())
print(eggs.items())

picnicItems = {'apples': 3, 'cups': 2}
print('I am bringing {} cups.'.format(str(picnicItems.get('cups', 0))))
print('I am bringing {} eggs.'.format(str(picnicItems.get('eggs', 0))))

spam = {'name': 'Pooky', 'age': 5}
spam.setdefault('color', 'black')
print
