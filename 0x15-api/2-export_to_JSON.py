#!/usr/bin/python3
"""Using what you did in the task #0,
   extend your Python script to export
   data in the JSON format"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com"
    userid = int(argv[1])
    user = requests.get(URL + "/users/{}".format(userid))
    todos = requests.get(URL + '/todos')
    name = user.json().get('username')
    jsonfile = argv[1] + '.json'

    data = dict()
    data[str(userid)] = []

    for todo in todos.json():
        if todo.get('userId') == userid:
            data[str(userid)].append(
                {
                    "task": todo['title'],
                    "completed": todo['completed'],
                    "username": name
                }
            )

    with open(jsonfile, 'w', newline='') as f:
        json.dump(data, f)
