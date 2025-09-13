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
    load_task()
    # case1 , if task is referred by its number 
    if isinstance(ref, int):
        if 0 <= ref < len(tasks):
            removed_task = tasks.pop(ref)
            save_task()
            return f"Task '{removed_task['Task']}' was removed"
        else:
            return f"Invalid task number: {ref}"
        
    # case2 , if task is referred by its name
    elif isinstance(ref, str):
        for i, task in enumerate(tasks):
            if ref.lower() in task['Task'].lower():
                removed_task = tasks.pop(i)
                save_task()
                return f"Task '{removed_task['Task']}' was removed"


#mark task as completed
def mark_task(ref):
    load_task()
    
    #case1, is id task is referred by its number
    if isinstance(ref, int):
        if 0 <= ref < len(tasks):
            tasks[ref]['Status'] = 'completed'
            save_task()
            return f"Task '{tasks[ref]['Task']}' is marked as completed"
        else:
            return f"Invalid task number: {ref}"
        
    #case2, if task is referred by its name
    if isinstance (ref, str):
        for i, task in enumerate(tasks):
            if ref.lower() in task['Task'].lower():
                tasks[i]['Status'] = 'completed'
                save_task()
                return f"Task '{tasks[i]['Task']}' is marked as completed"