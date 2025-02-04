# this program checks if the user imputs a prime number or not 
import math 

def is_prime(num=int):
  if num < 1:
    return False 
  for i in range(2,int(math.sqrt(num + 1))):
    if num % i == 0:
      return False
  return True

num = int(input('Enter a prime number: '))
if is_prime(num):
  print(f'{num} is a prime number.')
else:
  print(f'{num} is not a prime number')
