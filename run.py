"""
Start of the Project and File
"""
import numbers
import os
import sys
from tkinter.tix import TEXT  # To clear the console
import datetime  # To get the hour of the day
import time  # To give a delay when typing
import colorama # Import Colors into project
from colorama import Fore
from colored import fg, bg, attr
from text import *
colorama.init()

#Global Var for the username, age and location
USERNAME = ""

def main_menu():
    """
    This will be the landing, the user will first see this page before entering the game.
    """
    clear()
    print(TITLE)
    print(MAIN_TEXT)

    while True:
        answer = input(
            f"To start The game, type {Fore.BLUE}start{Fore.WHITE}. "
            f"If you want to know more about the game and how to play this game"
            f"type {Fore.BLUE}Info/Information{Fore.WHITE} "
            f"If you want to exit the application, just type {Fore.BLUE}exit{Fore.WHITE}\n" +
            "Answer: "
        )
        if answer in ("start", "strt"):
            start_game()
        elif answer in ("exit"):
            exit_app()
        elif answer in ("info", "information", "i"):
            information_menu()
        else:
            wrong_input(answer)

def get_username():
    """
    This function will retreive the username that the user will enter.
    """
    while True:
        name = input("What should I call you?\n" + "Answer: ").upper().strip()
        if len(name) < 2:
            print("The Length of the username is too short, please try again")
        elif len(name) > 15:
            print("The username is too long, try a shorter username.")
        elif any(char.isdigit() for char in name):
            print("The username cannot contain any numbers.")
        elif all(char.isalpha() or char.isspace() for char in name):
            global USERNAME
            USERNAME = " ".join(name.split()).title()
            break
        else:
            print("Your name cannot contain any symbols, please try again.")

def start_game():
    """
    When the user answers 'start' this function will run and the user
    can start playing the game.
    """
    clear()
    type_delay("Game is starting...\n")
    get_username()

    print(ROOM_DESIGN)
    type_delay(USERNAME + STORY_START)

    while True:
        # MULTIPLE TERMS AS BROTHER WHEN HE COMES BACK
        term = "look"
        answer = input("Answer: ").lower()
        words = answer.split()
        while True:
            if term in words:
                clear()
                print(ROOM_DESIGN)
                type_delay(f"Where do you look?\n"
                f"Forward{Fore.BLUE}(NORTH){Fore.WHITE}, "
                f"To Your Right{Fore.GREEN}(East){Fore.WHITE}, "
                f"Behind You{Fore.RED}(South){Fore.WHITE} "
                f"or to Your Left{Fore.YELLOW}(West){Fore.WHITE}\n")
                look_answer = input("Answer: ").lower()
                # When the user look to the North
                if look_answer in ("north", "n", "forward"):
                    clear()
                    print(ROOM_DESIGN_NORTH)
                    type_delay(f"{Fore.BLUE}{look_answer}:{Fore.WHITE}" +
                    " You see a door… What do you do?\n")
                    north_answer = input("Answer: ").lower()
                    # MULTIPLE TERMS AS KBROTHER WHEN HE COMES BACK
                    term_door = "inspect"
                    words_inspect = north_answer.split()
                    term_door_approach = "approach"
                    words_approach = north_answer.split()
                    term_door_open = "open"
                    words_open = north_answer.split()
                    # When the user inspect the door
                    if term_door in words_inspect:
                        type_delay(STORY_NORTH_INSPECT)
                        north_inspect_answer = input("Answer: ").lower()
                        while True:
                            if north_inspect_answer in ("y", "yes"):
                                north_yes_input = int(input("Please enter the 4 digit code: "))
                                str_int = str(north_yes_input)
                                if north_yes_input == 3012:
                                    type_delay("You entered the 4 digit code,"
                                    " you fiddle with the lock and"
                                    " all of a sudden *CLICK*. You unlocked the door!")
                                    clear()
                                    print(ESCAPED_MSG)
                                    input("Press Enter to continue...")
                                    main_menu()
                                elif len(str_int) < 4:
                                    print(f"It is a 4 digit combination lock,"
                                    f" you entered {str_int}."
                                    f" That is {len(str_int)} digits,"
                                    " you need to enter a 4 digit code.")
                                elif len(str_int) > 4:
                                    print(f"It is a 4 digit combination lock, you entered {str_int}."
                                    f" That is {len(str_int)} digits, you need"
                                    " to enter a 4 digit code.")
                                elif int(north_yes_input) != int():
                                    print("Only numbers please")
                                else:
                                    print(wrong_input)
                            elif north_inspect_answer in ("n", "no"):
                                break
                    # When the user approach the door
                    elif term_door_approach in words_approach:
                        type_delay(STORY_NORTH_APPROACH)
                        north_inspect_answer = input("Answer: ").lower()
                        while True:
                            if north_inspect_answer in ("y", "yes"):
                                north_yes_input = int(input("Please enter the 4 digit code: "))
                                str_int = str(north_yes_input)
                                if north_yes_input == 3012:
                                    type_delay("You entered the 4 digit code,"
                                    " you fiddle with the lock and"
                                    " all of a sudden *CLICK*. You unlocked the door!")
                                    clear()
                                    print(ESCAPED_MSG)
                                    input("Press Enter to continue...")
                                    main_menu()
                                elif len(str_int) < 4:
                                    print(f"It is a 4 digit combination lock,"
                                    f" you entered {str_int}."
                                    f" That is {len(str_int)} digits,"
                                    " you need to enter a 4 digit code.")
                                elif len(str_int) > 4:
                                    print(f"It is a 4 digit combination lock, you entered {str_int}."
                                    f" That is {len(str_int)} digits, you need"
                                    " to enter a 4 digit code.")
                                else:
                                    print(wrong_input)
                            elif north_inspect_answer in ("n", "no"):
                                break
                    # When the user open the door
                    elif term_door_open in words_open:
                        type_delay(STORY_NORTH_OPEN)
                        north_inspect_answer = input("Answer: ").lower()
                        while True:
                            if north_inspect_answer in ("y", "yes"):
                                north_yes_input = int(input("Please enter the 4 digit code: "))
                                str_int = str(north_yes_input)
                                if north_yes_input == 3012:
                                    type_delay("You entered the 4 digit code,"
                                    " you fiddle with the lock and"
                                    " all of a sudden *CLICK*. You unlocked the door!")
                                    clear()
                                    print(ESCAPED_MSG)
                                    input("Press Enter to continue...")
                                    main_menu()
                                elif len(str_int) < 4:
                                    print(f"It is a 4 digit combination lock,"
                                    f" you entered {str_int}."
                                    f" That is {len(str_int)} digits,"
                                    " you need to enter a 4 digit code.")
                                elif len(str_int) > 4:
                                    print(f"It is a 4 digit combination lock, you entered {str_int}."
                                    f" That is {len(str_int)} digits, you need"
                                    " to enter a 4 digit code.")
                                else:
                                    print(wrong_input)
                            elif north_inspect_answer in ("n", "no"):
                                break
                    elif north_answer == "back":
                        break
                    else:
                        print(wrong_input)

                # When the user look to the East
                elif look_answer in ("east", "e", "right"):
                    clear()
                    print(ROOM_DESIGN_EAST)
                    type_delay(f"{Fore.GREEN}{look_answer}:{Fore.WHITE}" +
                    "You Turn to your right and see a big bookshelf"
                    " that is almost as wide as the wall. "
                    "What do you do?\n")
                    east_answer = input("Answer: ").lower()
                    # MULTIPLE TERMS AS KBROTHER WHEN HE COMES BACK
                    term_bookshelf_purple = "purple"
                    words_inspect = east_answer.split()
                    term_bookshelf_approach = "approach"
                    words_approach = east_answer.split()
                    term_move_open = "move"
                    words_open = east_answer.split()
                    # When the user inspect the door
                    # Last Stopped, continue from hereLast Stopped, continue from hereLast Stopped, continue from hereLast Stopped, continue from hereLast Stopped, continue from here
                    if term_bookshelf_purple in words_inspect:
                        type_delay(STORY_EAST_INSPECT)
                        term_bookshelf_purple = input("Answer: ").lower()
                        while True:
                            if term_bookshelf_purple in words_inspect:
                                print(INSPECT_BOOK_PURPLE)
                                term_knife = "knife"
                                word_term_knife = term_bookshelf_purple.split()
                            elif north_inspect_answer in ("n", "no"):
                                break
                    # When the user approach the door
                    elif term_bookshelf_approach in words_approach:
                        type_delay(STORY_NORTH_APPROACH)
                        north_inspect_answer = input("Answer: ").lower()
                        while True:
                            if north_inspect_answer in ("y", "yes"):
                                north_yes_input = int(input("Please enter the 4 digit code: "))
                                str_int = str(north_yes_input)
                                if north_yes_input == 3012:
                                    type_delay("You entered the 4 digit code,"
                                    " you fiddle with the lock and"
                                    " all of a sudden *CLICK*. You unlocked the door!")
                                    clear()
                                    print(ESCAPED_MSG)
                                    input("Press Enter to continue...")
                                    main_menu()
                                elif len(str_int) < 4:
                                    print(f"It is a 4 digit combination lock,"
                                    f" you entered {str_int}."
                                    f" That is {len(str_int)} digits,"
                                    " you need to enter a 4 digit code.")
                                elif len(str_int) > 4:
                                    print(f"It is a 4 digit combination lock, you entered {str_int}."
                                    f" That is {len(str_int)} digits, you need"
                                    " to enter a 4 digit code.")
                                else:
                                    print(wrong_input)
                            elif north_inspect_answer in ("n", "no"):
                                break
                    # When the user open the door
                    elif term_move_open in words_open:
                        type_delay(STORY_NORTH_OPEN)
                        north_inspect_answer = input("Answer: ").lower()
                        while True:
                            if north_inspect_answer in ("y", "yes"):
                                north_yes_input = int(input("Please enter the 4 digit code: "))
                                str_int = str(north_yes_input)
                                if north_yes_input == 3012:
                                    type_delay("You entered the 4 digit code,"
                                    " you fiddle with the lock and"
                                    " all of a sudden *CLICK*. You unlocked the door!")
                                    clear()
                                    print(ESCAPED_MSG)
                                    input("Press Enter to continue...")
                                    main_menu()
                                elif len(str_int) < 4:
                                    print(f"It is a 4 digit combination lock,"
                                    f" you entered {str_int}."
                                    f" That is {len(str_int)} digits,"
                                    " you need to enter a 4 digit code.")
                                elif len(str_int) > 4:
                                    print(f"It is a 4 digit combination lock, you entered {str_int}."
                                    f" That is {len(str_int)} digits, you need"
                                    " to enter a 4 digit code.")
                                else:
                                    print(wrong_input)
                            elif north_inspect_answer in ("n", "no"):
                                break
                    elif north_answer == "back":
                        break
                    else:
                        print(wrong_input)

                # When the user look to the South
                elif look_answer in ("south", "s", "behind", "behind me", "turn around"):
                    clear()
                    print(ROOM_DESIGN_SOUTH)
                    type_delay(f"{Fore.RED}{look_answer}:{Fore.WHITE}" +
                    "You See a table with two chairs on each side. What do you do?\n")
                # When the user look to the West
                elif look_answer in ("west", "w", "left"):
                    clear()
                    print(ROOM_DESIGN_WEST)
                    type_delay(f"{Fore.YELLOW}{look_answer}:{Fore.WHITE}" +
                    "You turn to your left, you see a desk. What do you do?\n")
                elif look_answer in ("exit", "quit"):
                    exit_app()
                else:
                    print(wrong_input)
            else:
                print("Invalid Answer, please try again...")
                break
def north_face():
    """
    When the user face north, this functino will be shown.
    """
    
# Helper Functions
def clear():
    """
    This will clear the terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def exit_app():
    """
    This function will return the time of day and the user will get a greeting
    depending on the time of day.
    """
    clear()
    print("\nAre you positive you want to quit the app?\n")
    while True:
        answer = input(
            f"Type {Fore.BLUE}Y{Fore.WHITE} if you want to quit the app "
            f"or type {Fore.BLUE}N{Fore.WHITE} if you want to stay and try again.\n"
        )
        if answer == "yes" or "YES" or "Y" or "y":
            print(GOODBYE)
            type_delay("Closing the application... Have a Nice day!")
            quit()
        elif answer == "no" or "NO" or "N" or "n":
            break
        else:
            wrong_input(answer)

def type_delay(text):
    """
    This Function will create a typewriter delay in the terminal
    when certain text is displaying.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.03)
    time.sleep(0.4)

def wrong_input(answer):
    """
    When the user gives an invalid input, the function will be called
    """
    clear()
    print(f"\t{Fore.RED}Wrong command: {Fore.WHITE}'{answer}' is not a valid command."
    f" Please try again.\n"
    )

def information_menu():
    """
    The details on how to play the game will be displayed.
    """
    clear()
    print(INFORMATION_TEXT)


main_menu()