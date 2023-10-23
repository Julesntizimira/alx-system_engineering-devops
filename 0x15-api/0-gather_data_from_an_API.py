#!/usr/bin/python3
'''a Python script that, using this REST API,
   for a given employee ID, returns information
   about his/her TODO list progress
'''
import json
import requests
from sys import argv


r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                 .format(argv[1]))
res = r.json()

res_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
todos = res_todos.json()

titles = []

for todo in todos:
    if todo.get('userId') == eval(argv[1]):
        titles.append(todo['title'])

print('Employee {} is done with tasks({}/{}):'
      .format(res.get('name'), len(titles), len(todos)))
for title in titles:
    print('\t {}'.format(title))
