#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python script
to export data in the CSV format.
"""

import csv
import json
import requests
from sys import argv

if __name__ == "__main__":
    try:
        user_id = argv[1]
        url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
        file_name = "{}.json".format(user_id)
    except IndexError:
        exit

    res = requests.get(url)
    res = res.json()
    user_name = "{}".format(res.get('username'))
    res = requests.get(url + "/todos")
    res = res.json()

    my_dict = {}
    my_dict[user_id] = []

    for task in res:
        task_dict = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user_name
        }
        my_dict[user_id].append(task_dict)

    with open(file_name, "w") as f:
        f.write(json.dumps(my_dict))
