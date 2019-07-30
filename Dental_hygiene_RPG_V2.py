##
# Dental_hygiene_RPG.py
# Author: Jarvis Warnock
# A game to help promote dental hygiene in the form of an RPG
# Created: 03/07/19


def enemy_turn(player_health):
    print("")

def player_turn(player_health, enemy_health):
    player_health = player_health
    while repeat == True
        turn_option = input("""What would you like to do?:
(A)Attack
(H)Heal
""").title()
        if turn_option == 'A':
            chance = random.randint(1,4)
            attacks = input("""What attack would you like to use?
(1)Flossing - 10hp - 75%
(2)Brushing - 5hp - 100%
(3)Eat Healthy - 20hp - 25%
(4)Mouthwash - 15hp - 50%
""")

            #Flossing attack
            if attacks == '1':
                if chance > 1 and chance < 4:
                    enemy_health -= 10
                    print("Your flossing worked (-10hp)")
                elif chance == 4:
                    enemy_health -= 15
                    print("Your flossing worked and it was very effective (-15hp)")
                else:
                    print("Your flossing did not work")

            #Brushing attack
            elif attacks == '2':
                if chance == 4:
                    enemy_health -= 10
                    print("Your brushing worked and it was very effective (-10hp)")
                else:
                    enemy_health -= 5
                    print("Your brushing worked (-5hp)")

            #Eating healthy attack
            elif attacks == '3':
                if chance == 4:
                    enemy_health -= 20
                    print("Eating healthy worked (-20hp)")
                else:
                    print("Eating healthy did not work")

            #Mouthwash attack
            elif attacks == '4':
                if chance > 2 and chance < 4:
                    enemy_health -= 15
                    print("Using mouthwash worked (-15hp)")
                elif chance == 4:
                    enemy_health -= 20
                    print("Using mouthwash worked and it was very effective (-20hp)")
                else:
                    print("Using mouthwash did not work")

            else:
                print("Please enter a valid option")
        elif turn_option == 'H':
            heal = input("""How would you like to heal?
(1)Get a new toothbrush - 15hp - 50%
(2)Go to the dentist - 5hp - 100%
""")
            if heal == '2':
                print("You went to the dentist (+5hp)")
                player_health += 5
            elif heal == '1':
                chance = random.randint(1,2)
                if chance == 1:
                    player_health += 15
                    print("The toothbrush worked (+15hp)")
                else:
                     print("The tootbrush did not help")
                    
                    
        else:
            print("Please enter a valid option")
    return(player_health, enemy_health)

def main():
    option = ""
    enemy_health = 100
    player_health = 100
    # Tells the user a small description of what the game is about
    print("In this game you will be tasked with stopping an evil wizard who is trying to bring bad dental hygiene upon the world. Use these special powers I am giving you to stop him!")
    while option != "Quit":
        option = input("Would you like to: (P) Play, (H) How to Play, or (Q) Quit\n").title()
        if option == "P":
            while player_health > 0 and enemy_health > 0:
                player_health, enemy_health = player_turn(player_health, enemy_health)
                print("Your health: {}".format(player_health))
                print("Enemy health: {}".format(enemy_health))
                
                #print("Your health: {}".format(player_health))
                #print("Enemy health: {}".format(enemy_health))
                
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




import random

main()
    
