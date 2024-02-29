import random
import os

# Start Game Functions.

# Attribution: Stack Overflow - Menu


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
    name = None
    while True:
        name = input("\n Please enter your name (Use alphanumeric only): ")
        if name.isalnum():
            break
        else:
            print(f"{name} is invalid. Please use alphanumeric only.")
    return name

# Clear Function


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")

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
    print(f"""============ Instructions for Elemental Fantasy I ==============
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
    input("Press ENTER to continue")
    clear()
    print(f"""============ Element levels for Elemental Fantasy I =============
    Every element starts at 5 attack power towards hitpoints
    After every successful the element which was successful
    will level up by 5 till it reaches 15.
    for example:
    If a player successfully lands his first attack
    with 'Fire' being at an attack power of 5
    The next turn the same element will now have an attack power of 10
    """)
    input("Press ENTER to continue")
    clear()
    print(f"""============ Element Rules for Elemental Fantasy I ============
    Each element has its strengths and weaknesses:
    Fire beats Wind & Lightning but is weak against Earth and Water.
    Lightning beats Wind & Water but is weak against Earth and Fire.
    Wind beats Water & Earth but is weak against Fire and Lightning.
    Water beats Earth & Fire but is weak against Wind and Lightning.
    Earth beats Lightning & Fire but is weak against Water and Wind.
    """)
    input("Press ENTER to continue")
    clear()

# Game Rules

# Attribution - Personal Tutor - Tutoring on python for creating game elements
# Attribution - Stack Overflow - creating  basic structure of project
# Attribution - Stack Overflow - creating  basic structure of project
# Attribution - Youtube: NeuralNine - creating basic structure of project


def display_element_levels():
    """
    Function which displays the current level of the players elements.
    """
    print("\n-------------------------------------------")
    print("Current Element Levels: ")
    for element, level in element_levels.items():
        print(f"{element}: Level {level}")
    print("\n-------------------------------------------")


elements = ["Fire", "Lightning", "Wind", "Water", "Earth"]

element_rules = {
    'Fire': {'win_against': ['Wind', 'Lightning']},
    'Lightning': {'win_against': ['Wind', 'Water']},
    'Wind': {'win_against': ['Water', 'Earth']},
    'Water': {'win_against': ['Fire', 'Earth']},
    'Earth': {'win_against': ['Lightning', 'Fire']},
}

element_levels = {
    'Fire': 1,
    'Lightning': 1,
    'Wind': 1,
    'Water': 1,
    'Earth': 1,
}

# Player & Computer hitpoint values

# Attribution - Personal Tutor - Tutoring on python for creating game elements
# Attribution - Stack Overflow - creating  basic structure of project
# Attribution - Stack Overflow - creating  basic structure of project
# Attribution - Youtube: NeuralNine - creating basic structure of project


def play_game(player_name):
    start_game(player_name)
    """
    Main game function which takes in player inputs against their hitpoints
    """
    player_hitpoints = 50
    computer_hitpoints = 50

    while player_hitpoints > 0 and computer_hitpoints > 0:
        display_element_levels()

        computer = random.choice(elements)
        player = input("\n Choose your element (Fire, Lightning, Wind, Water or Earth): ").capitalize()  # noqa

        if player not in elements:
            print(f"{player} is an invalid input. Please choose a valid element.")
            continue

        print(f"{player_name}'s choice: {player}")
        print(f"Computers choice: {computer}")
        print("-----------------------------------------")

        player_hitpoints, computer_hitpoints = element_hitpoint_reduction(player_name, player, computer, player_hitpoints, computer_hitpoints)  # noqa

        if player_hitpoints <= 0:
            print(f"{player_name} has lost Game Over.")
        elif computer_hitpoints <= 0:
            print(f"{player_name} has Won. Congratulations.")

# Start Game Functions

# Attribution - Personal Tutor - Tutoring on python for creating game elements
# Attribution - Stack Overflow - creating  basic structure of project
# Attribution - Stack Overflow - creating  basic structure of project
# Attribution - Youtube: NeuralNine - creating basic structure of project


def start_game(player_name):
    """
    Function used to display a message before starting the game.
    """
    print(f"\n Get ready to battle {player_name}... ")


def element_hitpoint_reduction(player_name, player_move, computer_move, player_hitpoints, computer_hitpoints):  # noqa
    """
    Function for which elements are chosen and hitpoints.
    """
    player_level = element_levels[player_move]
    computer_level = element_levels[computer_move]

    if computer_move in element_rules[player_move]['win_against']:
        computer_hitpoints -= 5 * player_level
        print(
            f"{player_name} chose {player_move} and "
            f"succesfully beat {computer_move}")
        print(f"Computer hitpoints reduced to {computer_hitpoints}")
        if player_level < 3:
            element_levels[player_move] += 1
    elif player_move in element_rules[computer_move]['win_against']:
        player_hitpoints -= 5 * computer_level
        print(
            f"Computer chose {computer_move} and "
            f"{player_name}'s {player_move} failed")
        print(f"{player_name}'s hitpoints reduced to {player_hitpoints}")
        if computer_level < 3:
            element_levels[computer_move] += 1
    else:
        print("Move Cancelled Out - no hitpoint reduction")

    print("\n-----------------------------------------")
    print(f"{player_name}'s HP: {player_hitpoints}")
    print(f"Computer's HP: {computer_hitpoints}")
    print("\n-----------------------------------------")

    return player_hitpoints, computer_hitpoints


if __name__ == "__main__":
    main()
