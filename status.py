import json
from os.path import exists as file_exists
from user import get_users

def show_status():
    if not(file_exists('data/expenses.json')):
        print("No reimbursement")
        return
    with open('data/expenses.json', 'r') as expensesFile:
        expenses = json.loads(expensesFile.read())
    users = get_users()
    reimbursements = dict()
    for user in users:
        reimbursements[user["name"]] = dict()
        for a in users:
            reimbursements[user["name"]][a["name"]] = 0
    for expense in expenses:
        for user in expense["users_involved"]:
            reimbursements[user][expense["spender"]] += float(expense["amount_per_user"])
            
    for a in users:
        for b in users:
            if (a != b and reimbursements[a["name"]][b["name"]] != 0):
                print(a["name"] + " owes " + b["name"]  + " " + str(reimbursements[a["name"]][b["name"]]) + "€")