##
# Dental_hygiene_RPG.py
# Author: Jarvis Warnock
# A game to help promote dental hygiene in the form of an RPG
# Created: 03/07/19


def enemy_turn(player_health):


def player_turn(player_health, enemy_health):


def main():
    import random
    option = ""
    enemy_health = 100
    player_health = 100
    # Tells the user a small description of what the game is about
    print("In this game you will be tasked with stopping an evil wizard who is trying to bring bad dental hygiene upon the world. Use these special powers I am giving you to stop him!")
    while option != "Quit":
        option = input("Would you like to: (P) Play, (H) How to Play, or (Q) Quit\n").title()
        if option == "P":
            while player_health > 0 and enemy_health > 0:
                player_turn(player_health, enemy_health)
                
        elif option == "H":
            print("""How to Play:
This is a turn based game where you will chose an action to preform such as attack or heal.
you will have to defeat the evil wizard by attacking him until he loses all of his health, while making sure that you stay healthy.""")
        elif option == "Q":
                while option == "Q":
                    check = "N"
                    # Confirms if the user want to quit the program
                    while check != "Yes":
                        check = input("Are you sure that you want to quit the program? (Y/N)").upper()
                        if check == "N":
                            option = ""
                            check = "Yes"
                        elif check == "Y":
                            check = "Yes"
                            option = "Quit"
                        else:
                            print("Please enter 'Y' or 'N'")
        else:
            print("Please enter a valid option")






main()
    
