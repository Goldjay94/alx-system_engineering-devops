#!/usr/bin/python3
"""This script exports data retrieved
from an api request in CSV format"""

if __name__ == '__main__':
    import csv
    import requests as rq
    from sys import argv

    user_id = argv[1] if argv[1:] else 1
    FILENAME = user_id + ".csv"
    url = 'https://jsonplaceholder.typicode.com/'
    user = rq.get(url + 'users/{}'.format(user_id)).json()
    tasks = rq.get(url + 'users/{}/todos'.format(user_id)).json()
    with open(FILENAME, 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        [writer.writerow([user_id, user.get('username'), task.get('completed'),
                          task.get('title')]) for task in tasks]
