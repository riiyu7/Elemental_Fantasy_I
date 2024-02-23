import random

# Start Game Functions.

# Attribution: Stack Overflow - Menu -  https://stackoverflow.com/questions/34192588/simple-menu-in-python-3

def main():
    print(" ---------------------------------")
    print("| Welcome to Elemental Fantasy I  |")
    print(" ---------------------------------")

    # Call function to get players name.

    player_name = input_player_name()

    print(f"Hello, {player_name}! Welcome to Elemental Fantasy I")
    print(f"Please choose one of the following options: ")

    # While loop to get menu options.

    while True:
        choice = get_menu_choice()

        if choice == 1:
            play_game(player_name)
        elif choice == 2:
            show_rules()
        elif choice == 3:
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

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
    The main menu which displays options for the user to choose.
    """
    print("\n Main Menu: ")
    print("1. Play Game!")
    print("2. Rules/Instructions")
    print("3. Quit Game")

def get_menu_choice():
    
    while True:
        main_menu()
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
    print(f"""==================== Instructions for Elemental Fantasy I ======================
    Gameplay: 
    You battle with the computer using the five available elements:
    Fire, Lightning, Wind, Water & Earth.
    The aim of the game is to pick from one of the 5 elements
    To deplete your enemies Hitpoints (HP) from 30 to 0.
    The player will take the first turn and depending
    On what the computer chooses the attack could either be:
    Successful - Hit reduced enemines HP
    Cancelled Out - Hit did no damage to player or computer
    Failed - Hit does no damge to enemines HP
    """)
    print(f"""==================== Element Rules for Elemental Fantasy I ======================
    Each element has its strengths and weaknesses: 
    Fire beats Wind & Lightning but is weak against Earth and Water.
    Lightning beats Wind & Water but is weak against Earth and Fire.
    Wind beats Water & Earth but is weak against Fire and Lightning.
    Water beats Earth & Fire but is weak against Wind and Lightning.
    Earth beats Lightning & Fire but is weak against Water and Wind.
    """)

# Game Rules

# Attribution - Personal Tutor - Tutoring on python for creating game elements.
# Attribution - Stack Overflow - creating structure of project - https://stackoverflow.com/questions/7863471/rock-paper-scissors-in-python
# Attribution - Youtube: NeuralNine - creating structure of project - https://www.youtube.com/watch?v=55tcf9AA9hQ

elements = ["Fire", "Lightning", "Wind", "Water", "Earth"]

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

# Player & Computer hitpoint values

# Attribution - Personal Tutor - Tutoring on python for creating game elements.
# Attribution - Stack Overflow - creating structure of project - https://stackoverflow.com/questions/7863471/rock-paper-scissors-in-python
# Attribution - Youtube: NeuralNine - creating structure of project - https://www.youtube.com/watch?v=55tcf9AA9hQ

"""
Hitpoints for both players
"""
player_hitpoints = 30
computer_hitpoints = 30

def play_game(player_name):
    start_game(player_name)
    """
    Main game function which takes in player inputs against their hitpoints
    """
    global player_hitpoints
    global computer_hitpoints

    while player_hitpoints > 0 and computer_hitpoints > 0:
        computer = random.choice(elements)
        player = input("\n Choose your element (Fire, Lightning, Wind, Water or Earth): ").capitalize()
        
        if player not in elements:
            print("Invalid input. Please choose a valid element.")
            continue
        
        print(f"{player_name}'s choice: {player}")
        print(f"Computers choice: {computer}")
        print("-----------------------------------------")

        element_hitpoint_reduction(player_name, player, computer)

        if player_hitpoints <= 0:
            print(f"{player_name} has lost Game Over.")
        elif computer_hitpoints <= 0:
            print(f"{player_name} has Won. Congratulations.")

# Start Game Functions

# Attribution - Personal Tutor - Tutoring on python for creating game elements.
# Attribution - Stack Overflow - creating structure of project - https://stackoverflow.com/questions/7863471/rock-paper-scissors-in-python
# Attribution - Youtube: NeuralNine - creating structure of project - https://www.youtube.com/watch?v=55tcf9AA9hQ

def start_game(player_name):
    """
    Function used to display a message before starting the game.
    """
    print(f"\n Get ready to battle {player_name}... ")

def element_hitpoint_reduction(player_name, player_move, computer_move):
    """
    Function for which elements are chosen and hitpoints 
    """
    global player_hitpoints
    global computer_hitpoints

    if computer_move in element_rules[player_move]['win_against']:
        computer_hitpoints -= 5
        print(f"{player_name} chose {player_move} and succesfully beat {computer_move}")
        print(f"Computer hitpoints reduced to {computer_hitpoints}")
    elif player_move in element_rules[computer_move]['win_against']:
        player_hitpoints -= 5
        print(f"Computer chose {computer_move} and {player_name}'s {player_move} failed")
        print(f"{player_name} hitpoints reduced to {player_hitpoints}")
    else:
        print("Move Cancelled Out - no hitpoint reduction")

    print("\n-----------------------------------------")
    print(f"{player_name}'s HP: {player_hitpoints}")
    print(f"Computer's HP: {computer_hitpoints}")
    print("\n-----------------------------------------")


if __name__ == "__main__":
    main()