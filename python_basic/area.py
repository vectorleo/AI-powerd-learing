# this programe allow it user to easly get the area of a rectangle 
# if the user input the length and the breath the area or perimeter will be provided

def area(length,breath):
  result = length * breath 
  return result

def perimeter(length,breath):
  result = 2 * (length + breath)
  return result

running = True

while running:
  userinput = input('enter the following commands(area,perimeter,quit)').lower()
  if userinput  == 'area':
    input1 = int(input('enter the length: '))
    input2 = int(input('enter the breath: '))
    print(area(input1,input2))
  elif userinput  == 'perimeter':
    input1 = int(input('enter the length: '))
    input2 = int(input('enter the breath: '))
    print(perimeter(input1,input2))
  elif userinput == 'quit':
    print('Thanks for using...')
    running = False
  else:
    print('Invalid input.')
  

