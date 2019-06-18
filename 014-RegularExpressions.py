import re

# having the r before the string tells python not to use escape characters
# raw strings
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 303-916-8683.')
print('Phone number found: ' + mo.group())

# regex groups
phoneNumTwoRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumTwoRegex.search('My number still is 303-916-8683')
print(mo.group(1))
print(mo.group(2))
print(mo.group())
print(mo.group(0))
print(mo.groups())
print(type(mo.groups()))
print(type(mo.group()))

# pipes baby
heroRegex = re.compile(r'Batman|Tina Fey') # search for both heroes to match
mo1 = heroRegex.search('Batman and Tina Fey') # only the first match will be found
print(mo1.group())
mo2 = heroRegex.search('Tina Fey is better than Batman because she is real')
print(mo2.group())
mo3 = heroRegex.findall('I have a huge crush on Tina Fey. Not so much with Batman.')
print(mo2.group())

# Use the pipe to match one of several patterns.  Like all of Batman's toys
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost it\'s wheel')
print(mo.group())

# optional matching with the question mark
print('===> The ? matching groups')
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group())

# optional matching with the asterisk 
# the group that precedes the * can match zero or any number of times.
print('===> The * sign matching groups')
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The adventures of Batwowowowoman')
print(mo3.group())

# optional matching with the + sign
# the group that precedes the + can match one or any number of times.
print('===> The + sign matching groups')
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The adventures of Batman')
print(mo1 == None)
mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The adventures of Batwowowowoman')
print(mo3.group())
