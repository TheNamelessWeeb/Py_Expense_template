from PyInquirer import prompt
from os.path import exists as file_exists
from json_file import create_json_file
import json

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    },
]


def get_users():
    usersFileName = "data/users.json"
    users = []
    if file_exists(usersFileName):
        usersFile = open(usersFileName, "r")
        users = json.loads(usersFile.read())
    return users

def add_user(*args):
    infos = dict()
    usersFileName = "data/users.json"
    mode = "a"
    if args:
        infos["name"] = args[0]
        mode = args[1]
        usersFileName = "test/data/users_test.json"
    else:
        infos = prompt(user_questions)
        
    if not(file_exists(usersFileName)):
        create_json_file(usersFileName)

    with open(usersFileName, "r") as usersFile:
        data = usersFile.readlines()
        data[-1] = (json.dumps(infos) + '\n')
        if (len(data) >= 3):
            data[-2] += ','
        data.append(']')
        
    with open(usersFileName, "w") as usersFile:
        usersFile.writelines(data)

    return infos["name"]