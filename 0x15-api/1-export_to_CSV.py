#!/usr/bin/python3

"""
extending the Python script to export data in the CSV format.
"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    site_url = "https://jsonplaceholder.typicode.com"
    user_id = int(sys.argv[1])
    data = requests.get(site_url + "/users/{}".format(user_id))
    todo_list = requests.get(site_url + '/todos')
    name = data.json().get('username')
    file_name = sys.argv[1] + '.csv'

    with open(file_name, mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL,
                            lineterminator='\n')
        for todo in todo_list.json():
            if todo.get('userId') == user_id:
                writer.writerow([user_id, name, str(todo.get('completed')),
                                todo.get('title')])
