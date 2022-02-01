#!/usr/bin/python3

"""
extending the Python script to export data in the CSV format.
"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    data = requests.get('https://jsonplaceholder.typicode.com/todos/').json()
    data2 = requests.get('https://jsonplaceholder.typicode.com/users').json()

    for i in data2:
        if i['id'] == int(argv[1]):
            EMPLOYEE_NAME = i['username']

    with open(argv[1] + '.csv', 'w', newline='') as file:
        wrt = csv.writer(file, quoting=csv.QUOTE_ALL)

        for i in data:
            row = []
            if i['userId'] == int(argv[1]):
                row.append(i['userId'])
                row.append(EMPLOYEE_NAME)
                row.append(i['completed'])
                row.append(i['title'])
                wrt.writerow(row)
