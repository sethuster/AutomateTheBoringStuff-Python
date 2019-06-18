# lists are passed by reference 
def eggs(something):
  something.append('hello')

spam = [1, 2, 3]
eggs(spam) #the reference to teh list is passed
print(spam) # [1, 2, 3, 'hello']

import copy #allows the copying of things
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
print(cheese)

spam = [[1, 2], ['C', 'D']]
cheese = copy.deepcopy(spam) # needed because our list contains list and we want to copy it
cheese[0][0] = 42
print(spam)
print(cheese)
