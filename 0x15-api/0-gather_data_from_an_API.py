#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID
"""

import requests
from sys import argv


if __name__ == '__main__':

    UserId = argv[1]
    User = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(UserId)).json()

    TODO = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                        format(UserId)).json()

    DONE_TASKS = requests.get('https://jsonplaceholder.typicode.com/'
                              'todos?userId={}&&completed=true'.
                              format(UserId)).json()

    EMPLOYEE_NAME = User['name']
    COMPLETED_TASK = len(DONE_TASKS)
    TOTAL_TASKS = len(TODO)

    print('Employee {} is done with tasks({}/{}):'.
          format(EMPLOYEE_NAME, COMPLETED_TASK, TOTAL_TASKS))

    for i in DONE_TASKS:
        print('\t {}'.format(i['title']))
