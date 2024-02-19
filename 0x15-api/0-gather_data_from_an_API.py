#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

if __name__ == "__main__":
    import requests
    import sys
    import json

    num_1 = 0
    num_tasks = 0
    id = sys.argv[1]

    t = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={id}')
    user = requests.get(f'https://jsonplaceholder.typicode.com/users?id={id}')
    for task in t.json():
        if task.get("completed") is True:
            num_1 += 1
        num_tasks += 1

    user_name = user.json()[0].get("name")
    print("Employee {} is done with tasks ({}/{}):".format(
        user_name, num_1, num_tasks))

    for task in t.json():
        if task.get("completed") is True:
            print("\t {}".format(task.get("title")))
