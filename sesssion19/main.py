# tasks = [
#     {'title': 'buy food', 'status': 'pendign'},
#     {'title': 'call mom', 'status': 'completed'},
#     {'title': 'post packet', 'status': 'deleted'}
# ]


import data_manager

tasks = data_manager.get()
if not tasks:
    tasks = []
    

def show_menu():
    print('\n\n\n-------------------')
    print('1- add task')
    print('2- view task')
    print('3- complete task')
    print('4- delete task')
    print('5- exit')

def add_task():
    task = input("Enter a new task: ")
    tasks.append(
        {
            'title': task,
            'status': 'pending'
        }
    )
    print('task is added')
    
def view_task():
    for index, item in enumerate(tasks):
        if item['status'] != 'deleted':
            print(f'({index})- {item.get('title')} ({item.get('status')})')
        

def complete_task():
    view_task()
    task_id = int(input('which task to complete: '))
    tasks[task_id]['status'] = 'completed'
    


def delete_task():
    view_task()
    task_id = int(input('which task to delete: '))
    tasks[task_id]['status'] = 'deleted'

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        match choice:
            case '1':
                add_task()
            case '2':
                view_task()
            case '3':
                complete_task()
            case '4':
                delete_task()
            case '5':
                data_manager.set(tasks)
                break
            case _:
                print('invalid input')

main()

