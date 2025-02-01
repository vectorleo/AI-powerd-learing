# this program changes the multiples of 3 to fizz and mutiple of 5 to buzz

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for number in nums:
  if number % 3 == 0:
    print('Fizz')
  elif number % 5 == 0:
    print('Buzz')
  else:
    print(number)
