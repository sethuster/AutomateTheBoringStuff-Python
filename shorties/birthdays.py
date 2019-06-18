birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Kylie': 'Apr 17'}

while True:
  print('Enter a name: (blank to quit)')
  name = input()
  if name == '':
    break
  
  if name in birthdays:
    print('{} is the birthday of {}'.format(birthdays[name], name))
  else:
    print('I do not have a birthday for {}'.format(name))
    print('What is their birthday?')
    bday = input()
    birthdays[name] = bday
    print('Birthday database updated.')
