def hello():
  print('Howdy!')
  print('Howdy!!')
  print('Howdy!!!')

hello()

def hello(name):
  print('Howdy {}'.format(name))

hello('Tina')

def addShit(n1, n2):
  return n1 + n2

print(addShit(3, 5))

# Functions can have keywords - that's pretty neat
print('hello', end=' ')
print('world')

print('cats', 'dogs', 'mice', sep=', ')
