#!/usr/bin/python3

"""
dict of all todos
"""

import json
import requests
import sys


def to_json():
    user_todo = requests.get(
            f"https://jsonplaceholder.typicode.com/todos",
            params={"_expand": "user"}).json()

    data = []
    usrs = {}

    for ut in user_todo:
        USER_ID = ut.get("userId")
        EMPLOYEE_USERNAME = ut.get("user").get("username")

        if data != [] and EMPLOYEE_USERNAME != data[-1].get("username"):
            data = []

        data.append({"task": ut.get("title"),
                     "completed": ut.get("completed"),
                     "username": EMPLOYEE_USERNAME})

        usrs.update({USER_ID: data})

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(usrs, f)


if __name__ == "__main__":
    to_json()
