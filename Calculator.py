import os


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def calculate(firnum, oper, secnum):
    firnum = float(firnum)
    secnum = float(secnum)
    res = 0.0
    if oper == '+':
        res = firnum + secnum
    elif oper == '-':
        res = firnum - secnum
    elif oper == '*':
        res = firnum * secnum
    elif oper == '/':
        res = firnum / secnum
    else:
        print("Not a recognised operator")
    return res


while True:
    res = int(input("What's the first number?: "))
    print("+\n-\n*\n/")
    decision = 'y'
    while decision == 'y':
        oper = input("Pick an operation: ")
        secnum = int(input("What's the next number?: "))
        res = calculate(res, oper, secnum)
        decision = input(f"Type 'y' to continue calculating with {res}, or 'n' for new operation")
        clear_terminal()
