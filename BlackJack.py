import random, os

#Have you ever played Blackjack?? This is that game. If you haven't Google it(Can't describe cause it's big)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def addCard(your_card, comp_card, yourscore, compscore):
    while compscore < yourscore and compscore < 21:
        comp_card.append(random.choice(cards))
        compscore = sum(comp_card)
    return comp_card


def printScore(your_card, comp_card, yourscore, compscore):
    print(f"Your final hand: {your_card}, final score: {yourscore}")
    print(f"Computer's final hand {comp_card}, final score: {compscore}")


def checkWinner(your_card, comp_card, yourscore, compscore):
    """
    Checks the score and decides the winner
    :param your_card:
    :param comp_card:
    :param yourscore:
    :param compscore:
    :return:
    """
    res = ""
    if yourscore > 21:
        res = "You went over. You lose😟"
    elif compscore > 21:
        res = "Computer went over. You won😁"
    elif compscore == yourscore:
        res = "Draw🙂"
    elif (your_card[0] == 11 and your_card[1] == 10) or (your_card[0] == 10 and your_card[1] == 11):
        res = "You got a blackjack🤩"
    elif (comp_card[0] == 11 and comp_card[1] == 10) or (comp_card[0] == 10 and comp_card[1] == 11):
        res = "Opponent got a blackjack🤯"
    elif yourscore > compscore:
        res = "You won😃"
    elif yourscore < compscore:
        res = "You lose😣"
    printScore(your_card, comp_card, yourscore, compscore)
    print(res)


def isBlackjack(your_card, comp_card):
    """
    Returns true if any player got a blackjack
    :param your_card:
    :param comp_card:
    :return:
    """
    res = False
    if (your_card[0] == 11 and your_card[1] == 10) or (your_card[0] == 10 and your_card[1] == 11):
        res = True
    if (comp_card[0] == 11 and comp_card[1] == 10) or (comp_card[0] == 10 and comp_card[1] == 11):
        res = True
    return res


wannaplay = 'y'

while wannaplay == 'y':
    wannaplay = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if wannaplay == 'n':
        break
    decision = 'y'
    clear_terminal()
    your_card = [random.choice(cards), random.choice(cards)]
    comp_card = [random.choice(cards), random.choice(cards)]
    while decision == 'y':
        yourscore = sum(your_card)
        compscore = sum(comp_card)
        print(f"Your cards: {your_card}, current score: {yourscore}")
        print(f"Computer's first card: {comp_card[0]}")
        if yourscore > 21 or compscore > 21:
            checkWinner(your_card, comp_card, yourscore, compscore)
            break

        if isBlackjack(your_card, comp_card):
            print("Hell Yeah")
            checkWinner(your_card, comp_card, yourscore, compscore)
            break

        decision = input("Type 'y' to get another card, type 'n' to pass: ")

        if decision == 'y':
            your_card.append(random.choice(cards))
        if decision == 'n':
            if compscore <= yourscore:
                comp_card = addCard(your_card, comp_card, yourscore, compscore)
            checkWinner(your_card, comp_card, yourscore, sum(comp_card))
