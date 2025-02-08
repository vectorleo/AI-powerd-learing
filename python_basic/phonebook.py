# this is a phone book programe that stores the name and number of a individual 

contacts = {}
quit_phone = False

def add_contact(contact = dict):
  name = input('Enter a name: ')
  number = input('Enter a cell number: ')
  contact[name] = number
  print('Done.')

def delete_contact(contact = dict):
  view_contact(contact)
  user_input = input('Enter a name')
  del contact[user_input]
  print('Done.')

def view_contact(contact= dict):
  print('a')
  for key in contact.keys():
    print(key)
    

def search_number(contact= dict):
  user = input('Enter a Name: ')
  for k,v in contact.items():
    if user == k:
      print(f'Name: {k}, Number: {v}')
    else:
      print('Contact not found.')

while quit_phone != True:

  userinput = input('Enter the following commamds(add,view,search,del,quit): ').lower()

  if userinput == 'add':
    add_contact(contacts)

  elif userinput == 'view':
    view_contact(contacts)

  elif userinput == 'search':
    search_number(contacts)

  elif userinput == 'del':
    delete_contact(contacts)

  elif userinput == 'quit':
    print('Thanks for using..')
    quit_phone = True

  else:
    print('Invaild command.')
