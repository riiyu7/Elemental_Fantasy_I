import random
import os
import colorama
from colorama import Fore, Back, Style
colorama.init()


# Clear Function


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    Attribution: Stack Overflow - Clear the terminal
    https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python
    """
    os.system("cls" if os.name == "nt" else "clear")


def main():
    """
    Function which displays welcome message and gets playeers name
    Attribution: Stack Overflow - creating basic menu
    https://stackoverflow.com/questions/34192588/simple-menu-in-python-3

    """
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
            clear()
        elif choice == 2:
            show_rules()
            clear()
        elif choice == 3:
            clear()
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
            clear()
            print("Invalid Input. Please enter a valid option.")


# Rules Functions

def show_rules():
    """
    Function which prints game rules/instructions.
    """
    clear()
    print(f"""============ Instructions for Elemental Fantasy I ==============
    Gameplay:
    You battle with the computer using the five available elements:
    Fire, Lightning, Wind, Water & Earth.
    The aim of the game is to pick from one of the 5 elements
    To deplete your enemies Hitpoints (HP) from 50 to 0.
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

# Game Rules & Elements


def display_element_levels():
    """
    Function which displays the current level of the players elements.
    Attribution: Personal Tutor - [Mosahidur R.] - tutoring on game elements.
    https://www.mytutor.co.uk/students/secure/tutors/2038828/  # noqa
    """
    print("\n-------------------------------------------")
    print("Current Element Levels: ")
    for element in elements:
        level = element_levels[element]
        coloured_element = add_coloured_elements(element)
        print(f"{coloured_element}: Level {level}")
    """
    for element, level in element_levels.items():
        print(f"{element}: Level {level}")
    print("\n-------------------------------------------")
    """


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

computer_element_levels = {
    'Fire': 1,
    'Lightning': 1,
    'Wind': 1,
    'Water': 1,
    'Earth': 1,
}


def add_coloured_elements(element):
    """
    Function to get coloured display of an element.
    Attribution: Personal Tutor - [Mosahidur R.] - Tutoring on Colorama
    https://www.mytutor.co.uk/students/secure/tutors/2038828/
    """
    colours = {
        'Fire': Fore.RED,
        'Lightning': Fore.YELLOW,
        'Wind': Fore.WHITE,
        'Water': Fore.BLUE,
        'Earth': Fore.GREEN,
    }

    return f"{colours[element]}{element}{Style.RESET_ALL}"

# Player & Computer hitpoint values


def play_game(player_name):
    clear()
    start_game(player_name)
    """
    Main Game function which calls several functions 
    for the functionality of the game.
    Attribution: Stack Overflow - creating structure of project
    https://stackoverflow.com/questions/7863471/rock-paper-scissors-in-python
    Attribution: Stack Overflow - creating structure of project
    https://stackoverflow.com/questions/51353831/how-to-create-a-rock-paper-scissors-program  # noqa
    Attribution: Youtube: NeuralNine - creating structure of project
    https://www.youtube.com/watch?v=55tcf9AA9hQ
    """
    player_hitpoints = 50
    computer_hitpoints = 50

    while player_hitpoints > 0 and computer_hitpoints > 0:
        display_element_levels()

        computer = random.choice(elements)
        player = input("\nChoose your element (Fire, Lightning, Wind, Water or Earth): ").capitalize()  # noqa
        clear()
        if player not in elements:
            print(
                f"{player} is an invalid input. "
                f"Please choose a valid element.")
            continue

        print(f"{player_name}'s choice: {add_coloured_elements(player)}")
        print(f"Computers choice: {add_coloured_elements(computer)}")
        print("-----------------------------------------")

        player_hitpoints, computer_hitpoints = element_hitpoint_reduction(player_name, player, computer, player_hitpoints, computer_hitpoints)  # noqa

        if player_hitpoints <= 0:
            print(f"{player_name} has lost Game Over.")
        elif computer_hitpoints <= 0:
            print(f"{player_name} has Won. Congratulations.")

# Start Game Functions


def start_game(player_name):
    """
    Function used to display a message before starting the game.
    """
    print(f"\n Get ready to battle {player_name}... ")


def element_hitpoint_reduction(player_name, player_move, computer_move, player_hitpoints, computer_hitpoints):  # noqa
    """
    Function for which elements are chosen aswell 
    as hitpoint reduction based on the move made.
    Attribution: Personal Tutor - [Mosahidur R.] - Asistance with lessons on the hitpoint reduction function  # noqa
    https://www.mytutor.co.uk/students/secure/tutors/2038828/
    Attribution: Stack Overflow - Asistance with creating hitpoint reduction function
    https://stackoverflow.com/questions/50473861/tracking-player-health-text-based-game-python  # noqa
    """
    player_level = element_levels[player_move]
    computer_level = computer_element_levels[computer_move]

    damage = 0

    if computer_move in element_rules[player_move]['win_against']:
        computer_hitpoints -= 5 * player_level
        computer_hitpoints = max(0, computer_hitpoints - damage)
        print(
            f"{player_name} chose {player_move} and "
            f"succesfully beat {computer_move}")
        print(f"Computer hitpoints reduced to {computer_hitpoints}")
        if player_level < 3:
            element_levels[player_move] += 1
    elif player_move in element_rules[computer_move]['win_against']:
        player_hitpoints -= 5 * computer_level
        player_hitpoints = max(0, player_hitpoints - damage)
        print(
            f"Computer chose {computer_move} and "
            f"{player_name}'s {player_move} failed")
        print(f"{player_name}'s hitpoints reduced to {player_hitpoints}")
        if computer_level < 3:
            computer_element_levels[computer_move] += 1
    else:
        print("Move Cancelled Out - no hitpoint reduction")

    print("\n-----------------------------------------")
    print(f"{player_name}'s HP: {player_hitpoints}")
    print(f"Computer's HP: {computer_hitpoints}")
    print("\n-----------------------------------------")

    return player_hitpoints, computer_hitpoints


if __name__ == "__main__":
    main()
