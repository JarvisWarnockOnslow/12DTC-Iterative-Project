##
# Dental_hygiene_RPG.py
# Author: Jarvis Warnock
# A game to help promote dental hygiene in the form of an RPG
# Created: 03/07/19


def enemy_turn(player_health):
    player_health = player_health
    choice = random.randint(1,4)
    chance = random.randint(1,4)
    
    if choice == 1:
        player_health -= 10
        print("The evil wizard used plaque (-10hp)\n")
    elif choice == 2:
        player_health -= 15
        print("The evil wizard used unhealthy food (-15hp)\n")
    elif choice == 3:
        if chance > 2 and chance <= 4:
            player_health -= 20
            print("The evil wizard used bleeding gums (-20hp)\n")
        else:
            print("The evil wizard tried to give you bleeding gums, and failed\n")
    elif choice == 4:
        if chance == 4:
            player_health -= 25
            print("The evil wizard used Holes in your teeth (-25hp)\n")
        else:
            print("The evil wizard tried to put holes in your teeth, and failed\n")
    time.sleep(1)
    return player_health
    

def player_turn(player_health, enemy_health):
    player_health = player_health
    repeat = True
    while repeat == True:
        turn_option = input("""What would you like to do?:
(A)Attack
(H)Heal
""").title()
        # If the player wants to attack
        if turn_option == 'A':
            chance = random.randint(1,4)
            attacks = input("""What attack would you like to use?
(1)Flossing - 10hp - 75% chance
(2)Brushing - 5hp - 100% chance
(3)Eat Healthy - 20hp - 25% chance
(4)Mouthwash - 15hp - 50% chance
""")

            #Flossing attack
            if attacks == '1':
                if chance > 0 and chance < 4:
                    enemy_health -= 10
                    print("Your flossing worked (-10hp)\n")
                elif chance == 4:
                    enemy_health -= 15
                    print("Your flossing worked and it was very effective (-15hp)\n")
                else:
                    print("Your flossing did not work\n")
                repeat = False

            #Brushing attack
            elif attacks == '2':
                if chance == 4:
                    enemy_health -= 10
                    print("Your brushing worked and it was very effective (-10hp)\n")
                else:
                    enemy_health -= 5
                    print("Your brushing worked (-5hp)\n")
                repeat = False

            #Eating healthy attack
            elif attacks == '3':
                if chance == 4:
                    enemy_health -= 20
                    print("Eating healthy worked (-20hp)\n")
                else:
                    print("Eating healthy did not work\n")
                repeat = False

            #Mouthwash attack
            elif attacks == '4':
                if chance > 2 and chance <= 4:
                    enemy_health -= 15
                    print("Using mouthwash worked (-15hp)\n")
                elif chance == 4:
                    enemy_health -= 20
                    print("Using mouthwash worked and it was very effective (-20hp)\n")
                else:
                    print("Using mouthwash did not work\n")
                repeat = False

            else:
                print("Please enter a valid option\n")
        # If the player wants to heal
        elif turn_option == 'H':
            heal = input("""How would you like to heal?
(1)Get a new toothbrush - 15hp - 50% chance
(2)Go to the dentist - 5hp - 100% chance
""")
            if heal == '2':
                print("You went to the dentist (+5hp)\n")
                player_health += 5
                repeat = False
            
            elif heal == '1':
                chance = random.randint(1,2)
                if chance == 1:
                    player_health += 15
                    print("The toothbrush worked (+15hp)\n")
                else:
                     print("The tootbrush did not help\n")
                repeat = False
                    
                    
        else:
            print("Please enter a valid option\n")
    time.sleep(1)
    return(player_health, enemy_health)

def main():
    option = ""
    # Tells the user a small description of what the game is about
    print("In this game you will be tasked with stopping an evil wizard who is trying to bring bad dental hygiene upon the world. Use these special powers I am giving you to stop him!")
    while option != "Quit":
        option = input("Would you like to: (P) Play, (H) How to Play, or (Q) Quit\n").title()
        if option == "P":
            enemy_health = 10
            player_health = 100
            points = 0
            enemy_no = 1
            highscore = 0
            while player_health > 0:
                print("Your health: {}".format(player_health))
                print("Enemy health: {}\n".format(enemy_health))
                print("Enemy Number: {}".format(enemy_no))
                print("Points: {}".format(points))
                print("Highscore: {}".format(highscore))
                print("<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>\n")
                player_health, enemy_health = player_turn(player_health, enemy_health)
                player_health = enemy_turn(player_health)
                if enemy_health <= 0:
                    enemy_health = 10 + (enemy_no * 5)
                    enemy_no += 1
                    points += 10 * enemy_health

            if player_health <= 0:
                print("You have been defeated by the evil dental forces. Your score was {}. Why not play again?".format(points))
                time.sleep(1)
                print("Battles like this happen everyday within our lives. Make sure that you brush your teeth, floss, eat health foods, and go to the dentist to make sure that you have a healthy life.")
                if highscore > score:
                    highscore = score
                
            time.sleep(5)
                
        elif option == "H":
            print("""How to Play:
This is a turn based game where you will chose an action to preform such as attack or heal.
You will have to defeat the horde of evil minions who are trying to spread bad dental hygiene.
The enemies will get harder as you go but the harder then enemy, the more points you get, so get out ther and try get a highscore!""")
            time.sleep(2)
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
import time

main()
    
