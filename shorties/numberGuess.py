import random
secretNumber = random.randint(1, 20)
print('Try and guess the number between 1 and 20. Ready?')

# interesting that I don't have to declare guessesTaken before using it
for guessesTaken in range(1, 7):
  print('Begin.')
  guess = int(input())

  if guess < secretNumber:
    print('Your guess is too low')
  elif guess > secretNumber:
    print('Your guess is to high')
  else:
    break

if guess == secretNumber:
  print('Good Job Foo, you guessed my number in {} guesses!'.format(guessesTaken))
else:
  print('Dude? You could not guess my number in {} it was {} - duh.'.format(guessesTaken, secretNumber))

