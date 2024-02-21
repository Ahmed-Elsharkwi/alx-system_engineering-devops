#!/usr/bin/python3

"""
script that, using this REST API, for a given employee ID
returns information about his/her list progress """

import requests
from sys import argv

if __name__ == '__main__':
    api_url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    response = requests.get(api_url + "users/{}".format(user_id))
    users = response.json()
    user_name = users['name']
    response = requests.get(api_url + 
            "todos?userId={}".format(user_id))
    tasks = response.json()
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
