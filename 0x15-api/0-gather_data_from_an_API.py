#!/usr/bin/python3
"""A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    try:
        url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    except IndexError:
        exit

    res = requests.get(url)
    res = res.json()
    user_deets = "Employee {} is done with tasks".format(res.get('name'))
    print(user_deets, end="")
    res = requests.get(url + "/todos")
    res = res.json()
    done = 0
    for task in res:
        if task.get('completed'):
            done += 1
    print("({}/{}):".format(done, len(res)))
    [print("\t {}".format(task.get('title')))
        if task.get('completed') else "" for task in res]

    # for task in res:
    #     if task.get('completed'):
    #         print("\t {}".format(task.get('title')))
