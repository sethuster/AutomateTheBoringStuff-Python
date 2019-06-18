# this is from chapter 8 but thought it was interesting enough to warrent it's own little file.
import shelve
shelfFile = shelve.open('./016-shelffile')
cats = ['Fuzzy Squish', 'Burberry', 'Q']
print('===> Writing file to shelf...')
shelfFile['cats'] = cats
shelfFile.close()

print('===> Read file from shelf...')
shelfFile = shelve.open('./016-shelffile')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()

print('===> Deleting the shelf...')
import os
os.remove('./016-shelffile.db')

print('===> Creating pprint module')
import pprint
cats = [{'name': 'Fuzzy Squish', 'desc': 'old'}, {'name': 'Q', 'desc': 'chubby'}]
pprint.pformat(cats)
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

print('===> importing the cats')
import myCats
print(myCats.cats)
os.remove('myCats.py')
