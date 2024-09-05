def  add_task(task, todo_list):
  todo_list.append(task)

todo_list = [(1,'First Task'),(2,"Second Task")]
def search(name):
  for item in todo_list:
    if item[1] == name:
      return item[0]
    
print(search("Second Task"))