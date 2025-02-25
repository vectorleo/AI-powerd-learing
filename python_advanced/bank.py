# this programe shows the basics of oop in pthon 
class BankAccount:
  def __init__(self,name,balance):
    self.name = name 
    self.balance = balance

  def deposit(self,amount):
    self.balance += amount

  def withdraw(self,amount):
    self.balance -= amount
    return f'{amount} has been withdrawn succesfully.'
    
  def get_balance(self):
    return self.balance


account_1 = BankAccount('james cook',10000)
account_2 = BankAccount('sarah rock',15000)


print(account_1.name)
account_1.deposit(1000)
print(account_1.balance)
account_1.withdraw(5000)
print(account_1.balance)
  
print(account_2.name)
account_2.deposit(1000)
print(account_2.balance)
account_2.withdraw(5000)
print(account_2.balance)
  