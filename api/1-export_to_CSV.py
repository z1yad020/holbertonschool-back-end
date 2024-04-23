#!/usr/bin/python3

"""
dict to csv
"""

import csv
import requests
import sys


def to_csv(id):
    user = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{id}").json()

    user_todo = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{id}/todos").json()

    EMPLOYEE_NAME = user.get("name")

    with open(f'{id}.csv', mode='w') as f:
        emp = csv.writer(f)

        for usr in user_todo:
            emp.writerow([id, EMPLOYEE_NAME,
                         usr.get("completed"),
                         usr.get("title")])


if __name__ == "__main__" and len(sys.argv) == 2:
    to_csv(int(sys.argv[1]))
