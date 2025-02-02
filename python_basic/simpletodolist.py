# this is a simple todo list
todo_list = []

quit_Todo = False

while quit_Todo != True:
  user_input = input('Enter a command(add,view,remove,quit,): ').lower()

  if user_input == 'add':
    task = input('Enter a task: ')

    todo_list.append(task)
  elif user_input == 'view':
    print(f'To-do list:{todo_list}')

  elif user_input == 'remove':
    if todo_list == None:
      print('there is nothing in the list.')

    else:
      for i in range(len(todo_list)):
        print(todo_list[i],i)
    task = int(input('input the number to del:'))
    del todo_list[task]

  elif user_input == 'quit':
    print('thanks for using.')
    quit_Todo = True
  
  else:
    print('invalid input.')