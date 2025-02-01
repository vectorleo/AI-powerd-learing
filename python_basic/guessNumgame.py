import random

secret_num = random.randint(1,10)
guess_limit = 6

while guess_limit > 0:
  userguess =int(input('guess a number form 1 to 10: '))
  if userguess < secret_num:
    print('Too low.')
    guess_limit - 1
  elif userguess > secret_num:
    print('Too high')
    guess_limit - 1
  else:
    print('Yeah you got it.')
    break
