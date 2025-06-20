import os


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def findMaximunBid(auction):
    maxBid = 0
    winner = ""
    for key in auction:
        if auction[key] > maxBid:
            winner = key
            maxBid = auction[key]
        else:
            continue
    print(f"The winner is {winner} with a bid of ${maxBid}")


auction = {}
while True:
    name = str(input("what is your name?:  "))
    amount = int(input("what's your bid?:  "))
    auction[name] = amount
    more = input("Anymore bidders? ").lower()
    if more == 'yes':
        clear_terminal()
        continue
    else:
        findMaximunBid(auction)
        break
