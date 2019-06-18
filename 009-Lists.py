#Lists are arrays
spam = ['spam', 'is', 'good']
print(spam)
print(spam[2])

multi = [[1, 2], ['three', 'four']]
print(multi)
print(multi[0][1])
# Negative indexes start at the end
print(spam[-1])

bigger = ['cat', 'bat', 'rat', 'elephant', 'Matt']
# slices of the list start index to 
print(bigger[1:3])
print(bigger[0:-2])

moreSpam = spam + bigger
print(moreSpam)
del moreSpam[-1]
print(moreSpam)

for i in range(len(moreSpam)):
  print('this is kind of janky {}'.format(moreSpam[i]))

for i in moreSpam:
  print('less janky? {}'.format(i))

print('fucker' in moreSpam)
print('rat' not in moreSpam)

# multiple assignment trick
cat = ['fat', 'orange', 'annoying']
size, color, disposition = cat
print(size)
print(color)

#index() append() insert() remove() sort()
print(moreSpam.index('rat'))
# print(moreSpam.index('dude')) # throws error if not in list

spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam)
spam.insert(1, 'qbot')
print(spam)
spam.remove('moose')
print(spam)
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)
