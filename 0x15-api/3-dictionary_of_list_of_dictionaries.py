#!/usr/bin/python3
"""
exports employee info to csv
"""
if __name__ == "__main__":
    import json
    import requests

    request = requests.get(f"https://jsonplaceholder.typicode.com/users/")
    data = {}
    for user in request.json():
        userId = user["id"]
        username = user["username"]
        requestTasks = requests.get(
            f"https://jsonplaceholder.typicode.com/todos/?userId={userId}"
        )
        with open("all.json", "w", encoding="UTF-8") as file:
            data[userId] = [
                    {
                        "username": username,
                        "task": dictionary.get("title"),
                        "completed": dictionary.get("completed"),
                    }
                    for dictionary in requestTasks.json()
                ]
            file.write(json.dumps(data))
