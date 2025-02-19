# this is a more advanced form of the todo list in the python basic_folder
# this add it to a .txt file

file = 'to-do.txt'

def add_task(file):
  task = input('Enter a task: ')
  with open(file,'r') as data_base:
    if data_base.read(1) == '':
      with open(file,'a') as data_base:
        data_base.write(f"{task}=incomplete\n")
    else:
      with open(file,'a') as data_base:
        data_base.write(f"{task}=incomplete\n")
  print('item has been added')
    

def update_task(file):
  updated_task = ''
  view(file)
  num = int(input("Enter the number of the task compeleted: "))
  with open(file ,"r+") as data_base:
    lines = data_base.readlines()
    breaking = lines[num - 1].split('=')
    updated_task = f'{breaking[0]}=complete\n'
    lines[num - 1] = updated_task
  with open(file,'w') as data_base:
    data_base.writelines(lines)
  print('item has been updated')


def delete_task(file):
  view(file)
  line_number = int(input('Enter the number of the line to delete: '))
  with open(file,'r') as data_base:
    lines = data_base.readlines()
  with open(file,'w') as data_base:
    for i, line in enumerate(lines,start=1):
      if i != line_number:
        data_base.write(line)
  print('item has been deleted')


def view(file):
  print('-----------to-do-----------')
  
  with open(file,'r') as data_base:
    if data_base.read(1) == '':
      print('the list is empty.')
    else:
      with open(file, 'r') as data_base:
        num = 0
        for i in data_base.readlines():
          num += 1
          new_line = i.split('\n')
          print(num,')',new_line[0])
      
  print('---------------------------')


quit_Todo = False

while quit_Todo != True:
  user_input = input('Enter a command(add,view,remove,update,quit): ').lower()

  if user_input == 'add':
    add_task(file)

  elif user_input == 'view':
    view(file)

  elif user_input == 'remove':
    delete_task(file)

  elif user_input == 'update':
    update_task(file)

  elif user_input == 'quit':
    print('thanks for using.')
    quit_Todo = True
  
  else:
    print('invalid input.')