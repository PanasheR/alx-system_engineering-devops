#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":
    data = requests.get('https://jsonplaceholder.typicode.com/todos/').json()
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    tasks = []
    data2 = requests.get('https://jsonplaceholder.typicode.com/users').json()

    for i in data2:
        if i.get('id') == int(argv[1]):
            EMPLOYEE_NAME = i.get('name')

    for i in data:
        if i.get('userId') == int(argv[1]):
            TOTAL_NUMBER_OF_TASKS += 1

            if i.get('completed') is True:
                NUMBER_OF_DONE_TASKS += 1
                tasks.append(i.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(
                                                        EMPLOYEE_NAME,
                                                        NUMBER_OF_DONE_TASKS,
                                                        TOTAL_NUMBER_OF_TASKS))

    for i in tasks:
        print("\t {}".format(i))
