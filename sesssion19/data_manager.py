# data_manager.py
import json

# data form file read --> tasks
def get():
    with open('session19/data.json', 'r') as f:
        return json.load(f)


# write data in file --> data.json
def set(tasks):
    with open('session19/data.json', 'w') as f:
        json.dump(tasks, f)