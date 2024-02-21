#!/usr/bin/python3

"""
script that, using this REST API, for a given employee ID
returns information about his/her list progress """


if __name__ == '__main__':
    import requests
    import sys


    user_id = sys.argv[1]

    user = requests.get(f'https://jsonplaceholder.typicode.com/users?id={user_id}')
    user_name = user.json()[0].get("name")
    t = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id))
    tasks = t.json()
    total_tasks = len(tasks)
    completed_tasks_counter = 0
    completed_tasks = []
    for task in tasks:
        if task['completed'] is True:
            completed_tasks_counter += 1
            completed_tasks.append(task['title'])
    print("Employee {} is done with tasks({}/{}):".format(
        user_name, completed_tasks_counter, total_tasks))
    for title in completed_tasks:
        print("\t {}".format(title))
