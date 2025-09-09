import json

tasks = []
fILENAME = "tasks.json"

# save tasks to the Filename
def save_task():
    with open(fILENAME, 'w') as file:
        json.dump(tasks, file, indent=4)


# load tasks from the Filename  
def load_task():
    global tasks
    try:
        with open(fILENAME, 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    except json.JSONDecodeError:
        tasks = []


# add task
def add_task(task : str):
    tasks.append({'Task':task, 'Status':'Pending'})
    save_task()
    return f"Task '{task}' was added"


# view tasks
def view_tasks():
    if not tasks:
        return "There is no tasks"
    else:
        output = "\n".join(f"{i+1}. {t['Task']} - {t['Status']}"for i, t in enumerate(tasks))
        return "Your To-DO list: \n" + output


# delete task
def delete_task(ref):
    
    # case1 , if task is referred by its number 
    if isinstance(ref, int):
        if 0 <= ref < len(tasks):
            removed_task = tasks.pop(ref)
            return f"Task '{removed_task['Task']}' was removed"
        else:
            return f"Invalid task number: {ref}"
        
    # case2 , if task is referred by its name
    elif isinstance(ref, str):
        for i, task in enumerate(tasks):
            if ref.lower() in task['Task'].lower():
                removed_task = tasks.pop(i)
                return f"Task '{removed_task['Task']}' was removed"