import uuid

def  add_task(task, todo_list):
  todo_list.append(task)

todo_list = [(1,'First Task',"task description"),(2,"Second Task","task description")]
def search(name):
  for item in todo_list:
    if item[1] == name:
      return item[0]

def display(list,id = 0):
  if id == 0:
    for item in todo_list:
      print(f"ID: {item[0]} Title: {item[1]} Description: {item[2]}")
  else:
    for item in todo_list:
      if item[0] == id:
        print(f"ID: {item[0]} Title: {item[1]} Description: {item[2]}")
display(todo_list,2)

def generate_unique_id():
    return uuid.uuid4()

def add_task(task: tuple, todo_list: list):
    todo_list.append(task)

def create_task(task_name: str, task_details: str) -> tuple:
    return (generate_unique_id(), task_name, task_details)

def delete_task(task: tuple, todo_list: list):
    todo_list.remove(task)
