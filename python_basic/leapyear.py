# this program check user input an finds out.

def leep_year(year):
  if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    return True
  else:
    return False
  
user = int(input('Enter a year: '))

if leep_year(user):
  print(f'{user} is a leap year')
else:
  print(f'{user} is not a leap year.')




