# an invetory management project with python 
# using a csv data base 

import csv
import os.path
from os import path

db = 'inventory.csv'
class Product:

  def __init__(self ,name ,price=float ,quantity = int, category=None):
    self.name = name
    self.price = price 
    self.quantity = quantity
    self.category = category

  def __str__(self):
    return self.name

  def get_details(self):
    return {'name':self.name, 'price':self.price, 'quantity':self.quantity,'category':self.category}

class Inventory:

  def __init__(self):
    self.products = []
    self.field_names = ['name','price','quantity','category']
    
  def add_product(self,prod):
    self.products.append(prod.get_details())

  def update_stock(self,file,name,quantity=int):
    updated_data = []
    with open(file,'r',newline='') as csv_file:
      reader = csv.DictReader(csv_file)
      for row in reader:
        if row['name'] == name:
          qantElem = row['quantity']
          qantElem = int(qantElem) + quantity
          row['quantity'] = str(qantElem)
        updated_data.append(row)
    with open(file,'w',newline='') as csv_file:
      writer = csv.DictWriter(csv_file, fieldnames = self.field_names)
      writer.writeheader()
      writer.writerows(updated_data)


  def remove_product(self,file,num):
    updated_data = []
    with open(file,'r',newline='') as csv_file:
      reader = csv.DictReader(csv_file)
      for i, row in enumerate(reader,start=1):
        if i != num:
          updated_data += row
    with open(file,'w',newline='') as csv_file:
      writer = csv.DictWriter(csv_file,fieldnames= self.field_names)
      writer.writeheader()
      writer.writerows(self.products)

    
  def load_data(self,file):
    with open(file,'r',newline='') as csv_file:
      reader = csv.DictReader(csv_file)
      for index , row in enumerate(reader,start=1):
        print(f'{index}) name:{row['name']}| price:{row['price']}| quantity:{row['quantity']}| category:{row['category']}')

  def save_data(self,file):
    with open(file,'a', newline='') as csv_file:
      appender = csv.DictWriter(csv_file,fieldnames = self.field_names)
      appender.writerows(self.products)



def main(file):
  invent = False

  while invent != True:
    store1 = Inventory()
    user_input = input('Enter a command(add,view,remove,update,search,quit): ').lower()

    if user_input == 'add':
      name = input('Enter thr product name:  ')
      price = float(input('Enter the price: '))
      quantity = int(input('Enter the number '))
      category = input('Enter the category the product belongs to: ')
      product1 = Product(name,price,quantity,category)
      store1.add_product(product1)
      store1.save_data(file)
      print('product was added successfully.')

    elif user_input == 'view':
      print('------------Inventory------------')
      store1.load_data(file)
      print('-------------------------------')

    elif user_input == 'remove':
      store1.remove_product(file)
      print('product was removed succesfully.')

    elif user_input == 'search':
      print('The search fuction comming soon.')

    elif user_input == 'update':
      name = input('Enter thr product name:')
      quantity = int(input('Enter the number '))
      store1.update_stock(file,name,quantity)
      print('Invetory updated successfully.')

    elif user_input == 'quit':
      print('thanks for using.')
      invent = True
    else:
      print('invalid input.')

if __name__ == '__main__':

  if path.exists(db) == True:
    main(db)

  elif path.exists(db) != True:
    with open(db,'w',newline='') as csv_file:
      writer = csv.DictWriter(csv_file,['name','price','quantity','category'])
      writer.writeheader()
    main(db)
  
