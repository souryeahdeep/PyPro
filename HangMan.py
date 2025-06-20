import random

word_list = ['mango', 'camel', 'baboon','nymph']

list_of_ele_to_guess = list(str(random.choice(word_list)))  #list of elements to guess
word_to_guess = "".join(list_of_ele_to_guess)  #word to guess

guessed_letters = ['_'] * len(list_of_ele_to_guess)
guessed_word = "".join(guessed_letters)

i = 6

while i != 0:
    print("Word to guess: ", "".join(guessed_letters))
    guessed_let = input("Guess a letter: ")
    if guessed_let in list_of_ele_to_guess:
        pos = list_of_ele_to_guess.index(guessed_let)
        guessed_letters[pos] = guessed_let
        print("".join(guessed_letters))
        list_of_ele_to_guess[pos]='_'
    else:
        i -= 1
        print(f"You guessed {guessed_let}, that's not in the word. You lose a life")
        print(f"{i}/6 lives left")

    if "".join(guessed_letters)==word_to_guess:
        print("Guessed the word correctly")
        break
if i==0:
    print(f"IT WAS {word_to_guess}! You lose")