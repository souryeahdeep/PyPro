import random, art, os
from game_data import data

score = 0


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def printCompetitors(compA, compB):
    print(f"Compare A: {compA["name"]}, a {compA["description"]},from {compA["country"]}")
    print(art.vs)
    print(f"Against B: {compB["name"]}, a {compB["description"]},from {compB["country"]}")


def result(choice, correct_choice):
    if correct_choice and choice == 'a' or not correct_choice and choice == 'b':
        return score + 1
    else:
        clear_terminal()
        print(art.logo)
        print(f"Sorry that wrong. Final Score : {score}")
        return -1


A = random.choice(data)
while score > -1:
    clear_terminal()
    print(art.logo)
    if score > 0:
        print(f"Your score is {score}")
    B = random.choice(data)
    printCompetitors(A, B)
    choice = input("Who is more popular? A or B ").lower()
    correct_choice = A["follower_count"] > B["follower_count"]
    A = B
    score = result(choice, correct_choice)
