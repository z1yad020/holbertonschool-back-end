#!/usr/bin/python3

"""
dict to json
"""

import json
import requests
import sys


def to_json(id):
    user = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{id}").json()

    user_todo = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{id}/todos").json()

    EMPLOYEE_USERNAME = user.get("username")

    data = []

    for ut in user_todo:
        data.append({"task": ut.get("title"),
                     "completed": ut.get("completed"),
                     "username": EMPLOYEE_USERNAME})

    with open(f'{id}.json', mode='w') as f:
        json.dump({id: data}, f)


if __name__ == "__main__" and len(sys.argv) == 2:
    to_json(int(sys.argv[1]))
