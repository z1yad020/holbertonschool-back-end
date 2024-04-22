#!/usr/bin/python3

"""
task 0 - fetching fake api
"""


import sys
import requests


def todos(id):
    user = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{id}").json()
    user_todo = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{id}/todos").json()

    EMPLOYEE_NAME = user.get("name")
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = len(user_todo)
    completed_titles = []

    for usr in user_todo:
        if usr.get("completed"):
            NUMBER_OF_DONE_TASKS += 1
            completed_titles.append(usr.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
         EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for ttls in completed_titles:
        print(f"\t {ttls}")


if __name__ == "__main__" and len(sys.argv) == 2:
    todos(int(sys.argv[1]))
