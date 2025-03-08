# this is a contact management program using the (CRUD) create read update and delete. without saving to a file

data_base = {}

def create(storage=dict):
  name = input('enter a name: ')
  contact = input('enter the phone number: ')
  storage[name] = contact

def read(storage=dict):
  for k,v in storage.items():
    print(f'{k}:{v}')

def update(storage=dict):
  name = input('enter a name: ')
  for i in storage:
    if i == name:
      update_num = input('enter a diffrent number: ')
      storage[name] = update_num
    else:
      print('could not complete.')

def search(storage=dict):
  name = input('enter a name your looking for: ')
  for i in storage:
    if name == i:
      print(storage[name])

def delete(storage=dict):
  read(storage)
  name = input('enter a name you want to delete: ')
  del storage[name]

quit_Todo = False

while quit_Todo != True:
  user_input = input('Enter a command(add,view,remove,update,search,quit): ').lower()

  if user_input == 'add':
    create(data_base)
    print('Contact added successfully.')

  elif user_input == 'view':
    print('------------contact------------')
    read(data_base)
    print('-------------------------------')

  elif user_input == 'remove':
    delete(data_base)
    print('Contact removed successfully.')

  elif user_input == 'update':
    update(data_base)
    print('Contact updated successfully.')

  elif user_input == 'search':
    search(data_base)

  elif user_input == 'quit':
    print('thanks for using.')
    quit_Todo = True
  
  else:
    print('invalid input.')