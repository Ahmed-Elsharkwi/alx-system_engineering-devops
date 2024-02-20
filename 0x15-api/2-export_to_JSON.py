#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    num_1 = 0
    num_tasks = 0
    id = sys.argv[1]

    t = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={id}')
    user = requests.get(f'https://jsonplaceholder.typicode.com/users?id={id}')
    for task in t.json():
        if task.get("completed") is True:
            num_1 += 1
        num_tasks += 1

    user_name = user.json()[0].get("username")

    with open(f'{id}.json', 'w') as file_name:
        dict_1 = {f"{id}": []}
        for task in t.json():
            task_title = task["title"]
            status = task["completed"]
            if status is True:
                status = "true"
            else:
                status = "false"
            dict_2 = {"task": f"{task_title}", "completed": f"{status}", "username": f"{user_name}"}
            dict_1[f"{id}"].append(dict_2)
        json.dump(dict_1, file_name)
