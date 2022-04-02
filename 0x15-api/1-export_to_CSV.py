#!/usr/bin/python3
"""Using what you did in the task #0,
   extend your Python script to export
   data in the CSV format"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    userid = int(argv[1])
    user = requests.get(url + "/users/{}".format(userid))
    todos = requests.get(url + '/todos')
    name = user.json().get('username')
    filename = argv[1] + '.csv'

    with open(filename, mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL,
                            lineterminator='\n')
        for todo in todos.json():
            if todo.get('userId') == userid:
                writer.writerow([userid, name, str(todo.get('completed')),
                                todo.get('title')])
