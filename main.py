from PyInquirer import prompt
from examples import custom_style_2
from expense import new_expense
from user import add_user
from status import show_status

def ask_option():
    main_option = {
        "type":"list",
        "name":"main_options",
        "message":"Expense Tracker v0.1",
        "choices": ["New Expense","Show Status","New User", "Exit"]
    }
    option = prompt(main_option)
    if (option['main_options']) == "New Expense":
        new_expense()
        ask_option()
    if (option['main_options']) == "New User":
        add_user()
        ask_option()
    if (option['main_options']) == "Show Status":
        show_status()
        ask_option()

def main():
    ask_option()

main()