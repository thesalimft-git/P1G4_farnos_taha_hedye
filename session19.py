# tasks = [
#     {'title': 'buy food', 'status': 'pendign,done,deleted'}
#     {'title': 'buy food', 'status': 'pendign,done,deleted'}
#     {'title': 'buy food', 'status': 'pendign,done,deleted'}
# ]



tasks = []

def show_menu():
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
    for item in tasks:
        print(f'1- {item.get('title')} ({item.get('status')})')
        

def complete_task():
    pass

def delete_task():
    pass

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
                break
            case _:
                print('invalid input')

main()



# 1- buy food (pending)
# 2- buy food (pending)
# [{'title': 'buy food', 'status': 'pending'},
#  {'title': 'call mom', 'status': 'pending'}]

