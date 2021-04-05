import json

with open('users.json', 'r') as json_file:
    data = json.load(json_file)
    for item in data:
        print(f"Name: {item.get('name')}\nAge: {item.get('age')}\n")