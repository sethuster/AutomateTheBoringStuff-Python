# The program has one function collatz that takes an argument of number
# If the number is even print number // 2
# if the number is odd return 3 * number + 1
def collatz(number):
  if (number % 2) == 0:
    return number // 2
  else:
    return 3 * number + 1

print('Let us try the smallest impossible problem')
print('Enter a number: ')
userNum = int(input())

while userNum != 1:
  userNum = collatz(userNum)
  print(userNum)

