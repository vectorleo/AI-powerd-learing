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




