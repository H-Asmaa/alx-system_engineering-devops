#!/usr/bin/python3
"""
A script that returns info about an employe using
a REST API
"""
if __name__ == "__main__":
	import json
	import requests
	from sys import argv


	employee_id = argv[1]
	request = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
	EMPLOYEE_NAME = request.json()["name"]
	requestTasks = requests.get(
		f"https://jsonplaceholder.typicode.com/todos/?userId={employee_id}"
	)
	TOTAL_NUMBER_OF_TASKS = len(requestTasks.json())
	NUMBER_OF_DONE_TASKS = 0
	TASK_TITLE = ""
	for dictionary in requestTasks.json():
		for key, val in dictionary.items():
			if key == "completed" and val is True:
				NUMBER_OF_DONE_TASKS += 1
				if TASK_TITLE:
					TASK_TITLE += "\n"
				TASK_TITLE += "\t"
				TASK_TITLE += f"{dictionary['title']}"
	print(
		f"Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS})"
	)
	print(TASK_TITLE)