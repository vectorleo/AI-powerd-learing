# this program creates a squence of number base on the nth term provided by the User

def fibonacci(num):
  list_num = [0,1]

  for i in range(num):
    list_num.append(list_num[-2] + list_num[-1])

  return list_num

user_input = int(input('Enter a number: '))
print(fibonacci(user_input))