# this is a calculator programe 
import math

def addition(num1,num2):
  result = num1 + num2
  return result

def subtraction(num1,num2):
  result = num1 - num2
  return result

def multiplication(num1,num2):
  result = num1 * num2
  return result

def division(num1,num2):
  result = num1 / num2
  return result

def square(num1):
  result = num1 * num1
  return result

def square_root(num1):
  result = math.sqrt(num1)
  return result

running = True

instruction = '''
              enter the following commands
              a: for addtion
              s: for substraction
              m: for multiplication
              d: for division
              sq: for square of the number
              sqr: for square root of a number
              exit: to shutdown the program
              '''

print(instruction)
while running:
  user_input = input('enter a command: ')
  if user_input == 'a':
    num1 = int(input('first number:'))
    num2 = int(input('second number: '))
    print(addition(num1,num2))
  elif user_input == 's':
      num1 = int(input('first number:'))
      num2 = int(input('second number: '))
      print(subtraction(num1,num2))
  elif user_input == 'm':
      num1 = int(input('first number:'))
      num2 = int(input('second number: '))
      print(multiplication(num1,num2))
  elif user_input == 'd':
      num1 = int(input('first number:'))
      num2 = int(input('second number: '))
      print(division(num1,num2))
  elif user_input == 'sq':
      num1 = int(input('first number:'))
      print(square(num1))
  elif user_input == 'sqr':
      num1 = int(input('first number:'))
      print(square_root(num1,num2))
  elif user_input == 'exit':
      print('thanks for using..')
      running = False
  else:
     print('invalid input')