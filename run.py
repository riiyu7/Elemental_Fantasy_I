# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

# Start Game Functions.
def main():
    print(" ---------------------------------")
    print("| Welcome to Elemental Fantasy I  |")
    print(" ---------------------------------")

    # Call function to get players name.

    player_name = input_player_name()

    print(f"Hello, {player_name}! Welcome to Elemental Fantasy I")
    print(f"Please choose one of the following options: ")

def input_player_name():

    """
    This function is used to get the player to input their name
    which will be used to personalise the experience.
    """

    name = input("\n Please enter your name: ")
    return name


# Menu Functions

def main_menu():
    print("\n Main Menu: ")
    print("1. Play Game!")
    print("2. Rules/Instructions")
    print("3. Quit Game")

def game_menu():

def rules_menu():

def menu_options():

def get_menu_choice():
    while True:
        try:
            choice = int(input("Option: "))
            return choice
        except ValueError:
            print("Invalid Input. Please enter a valid option.")

# Rules Functions

    def show_rules():
    """
    Function which prints game rules/instructions 
    """
    print("\nGame Instructions: ")
    print("\nIn Elemental Fantasy I, you battle with the computer using the five available elements:")
    print("\nFire, Lightning, Wind, Water & Earth.")
    print("\nThe aim of the game is to pick from one of the 5 elements to deplete your enemies hitpoints (HP) from 30 to 0.")
    print("\nThe player will take the first turn and depending on what the computer chooses the attack could either be successful, cancelled out or ineffective.")
    print("\nIf the attack is ineffective then the player will take damage to their HP.")
    print("\n---------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\nEach element has its strengths and weaknesses: ")
    print("\nFire beats Wind & Lightning but is weak against Earth and Water")
    print("\nLightning beats Wind & Water but is weak against Earth and Fire")
    print("\nWind beats Water & Earth but is weak against Fire and Lightning")
    print("\nWater beats Earth & Fire but is weak against Wind and Lightning")
    print("\nEarth beats Lightning & Fire but is weak against Water and Wind")

# Game Rules


# Start Game Functions

    def start_game():

    def element_hitpoint_reduction():






if __name__ == "__main__":
    main()