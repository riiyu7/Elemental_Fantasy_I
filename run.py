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
    """
    The main manu which displays options for the user to choose.
    """
    print("\n Main Menu: ")
    print("1. Play Game!")
    print("2. Rules/Instructions")
    print("3. Quit Game")

def game_menu():
    """
    The game manu which displays options for the user to choose.
    """
    print("\n Game Menu: ")
    print("1. Return to Main Menu")
    print("2. Quit Game")

def rules_menu():
    """
    The rules manu which displays options for the user to choose.
    """
    print("\n Rules Menu: ")
    print("1. Return to Main Menu")
    print("2. Quit Game")

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
    Function which prints game rules/instructions.
    """
    print("\nGame Instructions: ")
    print("\nyou battle with the computer using the five available elements:")
    print("\nFire, Lightning, Wind, Water & Earth.")
    print("\nThe aim of the game is to pick from one of the 5 elements.")
    print("\nTo deplete your enemies Hitpoints (HP) from 30 to 0.")
    print("\nThe player will take the first turn and depending") 
    print("\nOn what the computer chooses the attack could either be: ")
    print("\nSuccessful - Hit reduced enemines HP") 
    print("\nCancelled Out - Hit did no damage to player or computer") 
    print("\nIneffective - Hit does no damge to enemines HP")
    print("\n----------------------------------------------------------------")
    print("\nEach element has its strengths and weaknesses: ")
    print("\nFire beats Wind & Lightning but is weak against Earth and Water.")
    print("\nLightning beats Wind & Water but is weak against Earth and Fire.")
    print("\nWind beats Water & Earth but is weak against Fire and Lightning.")
    print("\nWater beats Earth & Fire but is weak against Wind and Lightning.")
    print("\nEarth beats Lightning & Fire but is weak against Water and Wind.")

# Game Rules

element_rules = {
    'Fire': {'win_against': ['Wind', 'Lightning']},
    'Lightning': {'win_against': ['Wind', 'Water']},
    'Wind': {'win_against': ['Water', 'Earth']},
    'Water': {'win_against': ['Fire', 'Earth']},
    'Earth': {'win_against': ['Lightning', 'Fire']},
}

# Level 1 Hitpoint:
element_hitpoints = {
    'Fire': 5,
    'Lightning': 5,
    'Wind':5, 
    'Water':5, 
    'Earth':5, 
}

#Fire Moves
if player == 'fire'
    print("computer lost (HP)")
    computer_hitpoints -= 5
elif player == 'fire' and (computer == 'earth' or computer == 'water'):
    print(f"{player_name} lost (HP)")
    player_hitpoints -=5

#Lightning Moves
elif player == 'Lightning' and (computer == 'wind' or computer == 'water'):
    print("computer lost (HP)")
    computer_hitpoints -= 5
elif player == 'Lightning' and (computer == 'earth' or computer == 'fire'):
    print(f"{player_name} lost (HP)")
    player_hitpoints -=5

#Wind Moves
elif player == 'Wind' and (computer == 'earth' or computer == 'water'):
    print("computer lost (HP)")
    computer_hitpoints -= 5
elif player == 'Wind' and (computer == 'lightning' or computer == 'fire'):
    print(f"{player_name} lost (HP)")
    player_hitpoints -=5

Add function rules for element Wind
#Water Moves

#Earth Moves

# Start Game Functions

    def start_game(player_name):

    def element_hitpoint_reduction():


if __name__ == "__main__":
    main()