def spam(divideBy):
  try:
    return 42 / divideBy
    # you could also just do except:
  except ZeroDivisionError:
    print('dude, the fuck?')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
