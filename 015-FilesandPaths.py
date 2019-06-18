import os
print(os.path.join('usr', 'bin', 'spam'))

print('===> Join a bunch of files')
myFiles = ['accounts.txt', 'details.csv', 'nonexistant.docx']
for filename in myFiles:
  print(os.path.join('users/ezo/bullshittery', filename))

print('===> The CWD')
print(os.getcwd())

print('===> Creating New Directories')
newFolder = os.path.join('/Users/ezo', 'created', 'folder')
print(newFolder)
os.makedirs(newFolder)
print('New folder created!')
os.removedirs(newFolder)
print('New folder deleted!')

print('===> Absolute path: ./')
print(os.path.abspath('./'))
print('===> is abs(./)')
print(os.path.isabs('./'))
print('===> relpath from / to here')
print(os.path.relpath('/Users', os.getcwd()))

print('===> Dirname of /Users/ezo/some/path')
print(os.path.dirname('/Users/ezo/some/path'))
print(os.path.basename('/Users/ezo/some/other/path'))
print(os.path.split('/Users/ezo/some/other/path'))
print('/Users/ezo/some/other/path'.split(os.path.sep))

print('===> File Sizes and Folder Contents')
print(os.path.getsize('./015-FilesandPaths.py'))
print(os.listdir('./'))

print('===> Open a file')
textFile = open('./015-textfile.txt').read()
print(textFile)
textFile = open('./015-textfile.txt')
print(textFile.readlines())

print('===> Writing a file')
baconFile = open('015-bacon.txt', 'w')
baconFile.write('This is a file.\nThere are many like it.\nBut this one is mine.\n')
baconFile.close()
baconFile = open('015-bacon.txt', 'a')
baconFile.write('Bacon is delicious.')
baconFile.close()
baconFile = open('015-bacon.txt')
print(baconFile.read())
baconFile.close()
os.remove('./015-bacon.txt')




