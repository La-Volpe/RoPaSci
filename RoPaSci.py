__author__ = 'Javad Arjmandi'
from random import randint
def player_choice_input():
    choice = input("Welcome to The Game! Please Choose: \n1. Rock\n2. Paper\n3. Scissor\n>>>")
    if choice == "1":
        return "Rock"
    elif choice == "2":
        return "Paper"
    elif choice == "3":
        return "Scissor"

def computer_choice():
    _random = randint(1,3)
    if _random == 1:
        return "Rock"
    elif _random == 2:
        return "Paper"
    elif _random == 3:
        return "Scissor"
def game():

    player = player_choice_input()
    cmp = computer_choice()
    pre_game_message = "You've chosen " + player + \
                      " and Computer has chosen " + cmp
    print(pre_game_message)
    print("\n.\nResult:\n")
    #Cases that The Player wins:

    #Cases that The Player loses:

    #Tie Cases:

game()