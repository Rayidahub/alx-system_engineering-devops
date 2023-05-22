Skip to content
Product
Solutions
Open Source
Pricing
Search
Sign in
Sign up
kwhit2
/
holberton-system_engineering-devops
Public
Code
Issues
Pull requests
Actions
Projects
Security
Insights
holberton-system_engineering-devops/0x15-api/0-gather_data_from_an_API.py /
@kwhit2
kwhit2 pep8 fix
Latest commit 796011b on May 3, 2021
 History
 1 contributor
Executable File  31 lines (29 sloc)  1.5 KB
 

#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID, returns
    information about his/her TODO list progress. Requirements:
    You must use urllib or requests module
    The script must accept an integer as a parameter, which is the employee ID
    The script must display on the standard output the employee TODO list...
    ...progress in this exact format: First line: Employee EMPLOYEE_NAME is...
    ...done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):,
    NUMBER_OF_DONE_TASKS: number of completed tasks, TOTAL_NUMBER_OF_TASKS:...
    ...total number of tasks, which is the sum of completed and non-completed..
    ..tasks Second and N next lines display the title of completed tasks:..
    ..TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE) """
import requests
from sys import argv


if __name__ == "__main__":
    userId = argv[1]
    name = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(userId)).json()
    # todo variable = grabs all todos (completed or not) for the user passed in
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(userId)).json()
    completed = []
    for task in todo:
        if task.get('completed') is True:
            completed.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(name.get('name'), len(completed), len(todo)))
    for task in completed:
        print("\t {}".format(task))
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
holberton-system_engineering-devops/0-gather_data_from_an_API.py at master · kwhit2/holberton-system_engineering-devops · GitHub
