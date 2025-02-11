# this is a more advanced form of the todo list in the python basic_folder
# this add it to a .txt file
# data_base.write(f"\n{task} , incomplete")

file = 'to-do.txt'

def add_task(file):
  with open(file,'a+') as data_base:
    task = input('Enter a task: ')
    if data_base.readlines() == None:
      data_base.write(f"{task} , incomplete")
    else:
      data_base.write(f"\n{task} , incomplete")
    

def update_task():
  pass
def delete():
  pass
def view(file):
  print('-----------to-do-----------')
  with open(file, 'r') as data_base:
   print(data_base.readline())
  print('---------------------------')

add_task(file)
view(file)

