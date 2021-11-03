from PyInquirer import prompt
from datetime import date
from user import add_user
from os.path import exists as file_exists
from json_file import create_json_file
import json

amount_question = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    }
]

label_question = [
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
]

def get_users():
    usersFileName = "data/users.json"
    users = []
    if file_exists(usersFileName):
        usersFile = open(usersFileName, "r")
        users = json.loads(usersFile.read())
    return users


def new_expense(*args):
    expensesFileName = "data/expenses.json"
    infos = dict()

    # amount and label
    infos["amount"] = prompt(amount_question)["amount"]
    try:
        amount = int(infos["amount"])
    except ValueError:
        print("please enter a valide number")
        return
    
    infos["label"] = prompt(label_question)["label"]
    
    #get user
    users =  get_users()
    users.append("Add User")
    
    #assign spender
    choose_spender = {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender",
        "choices": users
    }
    spender = prompt(choose_spender)["spender"]
    if spender == "Add User":
        infos["spender"] = add_user()
    else:
        infos["spender"] = spender
    infos["date"] = date.today().strftime("%d/%m/%Y")

    #add users
    while True:
        add_users = {
            "type":"list",
            "name":"add_users",
            "message":"New Expense - Add Users",
            "choices": ["Add User", "Select Users Involved"]
        }
        users = get_users()
        print("Current users:")
        for user in users:
            print(user["name"])
        add_users = prompt(add_users)["add_users"]
        if (add_users == "Add User"):
            add_user()
        else:
            break
    
    #select users involved
    users = get_users()
    users_involved = {
        "type":"checkbox",
        "name":"users_involved",
        "message":"New Expense - Select Users Involved",
        "choices": users
    }
    users_involved = prompt(users_involved)["users_involved"]
    infos["users_involved"] = users_involved
    infos["amount_per_user"] = int(infos["amount"]) / len(users_involved)


    if not(file_exists(expensesFileName)):
        create_json_file(expensesFileName)

    with open(expensesFileName, "r") as expensesFile:
        data = expensesFile.readlines()
        data[-1] = (json.dumps(infos) + '\n')
        if (len(data) >= 3):
            data[-2] += ','
        data.append(']')
        
    with open(expensesFileName, "w") as expensesFile:
        expensesFile.writelines(data)
    return True


