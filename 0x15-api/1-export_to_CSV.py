#!/usr/bin/python3

"""
extending the Python script to export data in the CSV format.
"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    data_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user = requests.get(data_url, verify=False).json()
    data_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)
    too_list = requests.get(data_url, verify=False).json()
    with open("{}.csv".format(user_id), 'w', newline='') as f:
        tasks = csv.writer(f, quoting=csv.QUOTE_ALL)
        for t in todo:
            tasks.writerow([int(user_id), user.get('username'),
                                 t.get('completed'),
                                 t.get('title')])