#!/usr/bin/python3
"""Using what you did in the task #0,
   extend your Python script to export
   data in the JSON format"""
import json
import requests


if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com"
    users = requests.get(URL + '/users/')
    todos = requests.get(URL + '/todos')
    jsonfile = 'todo_all_employees.json'

    data = dict()
    for user in users.json():
        userid = user['id']
        username = user['username']
        data[str(userid)] = []
        for todo in todos.json():
            if todo.get('userId') == userid:
                data[str(userid)].append(
                    {
                        "username": username,
                        "task": todo['title'],
                        "completed": todo['completed']
                    }
                )

    with open(jsonfile, 'w', newline='') as f:
        json.dump(data, f)
