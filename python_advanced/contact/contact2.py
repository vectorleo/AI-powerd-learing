# so this is an imporved version of the contact programe 
# saving user data are done in a csv file 

import csv
import os.path 
from os import path

file = 'data.csv'

def add(f,n,c): # f = file, n = name, c = contact details 
  '''
  f = the file to store data
  n = name to add to the contactbook program
  c = the contact it self 
  '''  
  with open(f,'a',newline='') as csv_file:
    writer = csv.DictWriter(csv_file,['Name','contact info'])
    writer.writerow({'Name':n,'contact info':c})
    

def delete(f):
  read(f)
  updated_data = []
  num = int(input('Enter the number you would like to delete: '))
  with open(f,'r',newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for i,reader in enumerate(reader,start=1):
      if i != num:
        updated_data.append(reader)
  with open(f,'w',newline='') as csv_file:
    writer = csv.DictWriter(csv_file,['Name','contact info'])
    writer.writeheader()
    writer.writerows(updated_data)

    
def update(f):
  read(file)
  updated_data = []
  found = False
  name = input('what is name of the contact you would like to update: ')
  contact = input('Enter a the details: ')
  with open(file,'r',newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
      if row['Name'] == name:
        row['contact info'] = contact
        found = True
      else:
        found = False
      updated_data.append(row)

    if found == False:
      print('the contact inputed was wrong')
    elif found == True:
      print('Done.')
  with open(f,'w',newline='') as csv_file:
    writer = csv.DictWriter(csv_file,['Name','contact info'])
    writer.writeheader()
    writer.writerows(updated_data)


def read(f):
  with open(f,'r',newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for index,row in enumerate(reader,start=1):
      print(index,')',row['Name'],':',row['contact info'])


def search(f):
   name = input('Enter the contact your looking for: ')
   isdisplayed = False
   with open(f,'r',newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
      if row['Name'] == name:
        print('this contact number is',row['contact info'])
        isdisplayed = True
    if isdisplayed == False:
      print('contact not found')
      action = input('would like to add that to the contact list? y for yes, n for no').lower()
      if action == 'y':
        contact = input('enter the contact details: ')
        add(f,name,contact)
      elif action == 'n':
        pass
      else:
        print('invalid input.')

def main(file):
  contact_app = False

  while contact_app != True:
    user_input = input('Enter a command(add,view,remove,update,search,quit): ').lower()

    if user_input == 'add':
      name = input('Enter a name:')
      contact = input('Enter the number ')
      add(file,name,contact)
      print('Contact added successfully.')

    elif user_input == 'view':
      print('------------contact------------')
      read(file)
      print('-------------------------------')

    elif user_input == 'remove':
      delete(file)
      print('contact was removed succesfully.')

    elif user_input == 'update':
      update(file)
      print('Contact updated successfully.')

    elif user_input == 'search':
      search(file)

    elif user_input == 'quit':
      print('thanks for using.')
      contact_app = True
  
    else:
      print('invalid input.')


if __name__ == '__main__':

  if path.exists(file) == True:
    main(file)

  elif path.exists(file) != True:
    with open(file,'w',newline='') as csv_file:
      writer = csv.DictWriter(csv_file,['Name','contact info'])
      writer.writeheader()
    main(file)
  