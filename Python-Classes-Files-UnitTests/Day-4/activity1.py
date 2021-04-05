import json
'''
user = {}

user['name'] = input("Enter name: ")
user['age'] = int(input("Enter age: "))

with open('person.json', 'w') as output:
    json.dump(user, output)
'''
database = {}
database["users"] = []

while True:
    with open('users.json', 'w') as output:
        user = {}
        user['name'] = input("Enter name: ")
        user['age'] = int(input("Enter age: "))
        database['users'].append(user)
        json.dump(database, output)

    choice = input("Enter q to quit: ")
    if choice == 'q':
        break