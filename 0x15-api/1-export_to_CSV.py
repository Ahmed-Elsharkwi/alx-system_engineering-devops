#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

if __name__ == "__main__":

    import csv
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

    name = user.json()[0].get("name")
    user_name = user.json()[0].get("username")

    with open(f'{id}.csv', mode='w') as employee_file:
        employee_writer = csv.writer(
                employee_file, delimiter=',', quoting=csv.QUOTE_ALL)

        for task in t.json():
            status = task.get("completed")
            title = task.get("title")
            employee_writer.writerow(
                    [f"{id}", f"{user_name}", f"{status}", f"{title}"])
