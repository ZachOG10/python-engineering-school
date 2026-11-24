balance = 10000
def deposit(balance, amount):
    new_balance = balance + amount
    return new_balance

def withdraw(balance, amount):
    remaining_balance = balance - amount
    return remaining_balance

def display_balance(balance):
    print(balance)
balance = deposit(balance, 5000)
balance = withdraw(balance, 3000)
display_balance(balance)
