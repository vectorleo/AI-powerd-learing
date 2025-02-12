# this is a more advanced form of the todo list in the python basic_folder
# this add it to a .txt file
# data_base.write(f"\n{task} , incomplete")

file = 'to-do.txt'

def add_task(file):
  task = input('Enter a task: ')
  with open(file,'r') as data_base:
    if data_base.read(1) == '':
      with open(file,'a') as data_base:
        data_base.write(f"{task} , incomplete")
    else:
      with open(file,'a') as data_base:
        data_base.write(f"\n{task} , incomplete")
    

def update_task(file):
  view(file)
  num = input("Enter the number of the task compeleted: ")
  with open(file, 'r') as data_base:
    lines = data_base.readlines()
    lines[num] = 'kdfl'

def delete_task(file):
  view(file)
  action = int(input('Enter the number of the line to delete: '))
  with open(file,'r') as data_base:
    line = data_base.readlines()

  del line[action - 1]

  with open(file,'w') as data_base:
    data_base.write(file)
  
  print('Task deleted.')


def view(file):
  print('-----------to-do-----------')
  with open(file, 'r') as data_base:
   num = 0
   for i in data_base.readlines():
     num += 1
     print(num,')',i)
  print('---------------------------')

add_task(file)
view(file)
delete_task(file)
