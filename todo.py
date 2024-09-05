import uuid

def generate_unique_id():
    return uuid.uuid4()

def add_task(task: tuple, todo_list: list):
    todo_list.append(task)

def create_task(task_name: str, task_details: str) -> tuple:
    return (generate_unique_id(), task_name, task_details)

  
