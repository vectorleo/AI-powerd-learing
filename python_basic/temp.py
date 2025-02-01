# this programme use conditional statements to check the temperature 

temp = int(input('what is the temperature(c*): '))

if temp < 25:
  print('Wow that cold, Do wear a sweeter.')
elif temp > 47:
  print('Wow thats hot!')
else:
  print('Its just rigth.')