"""
Start of the Project and File
"""
from asyncio import constants
import numbers
import os
from symbol import term
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
        answer = input("Answer: ").lower()
        while True:
            first_scenario = "look"
            first_scenario_app = "approach"
            first_scenario_ins = "inspect"
            if first_scenario in answer or first_scenario_app in answer or first_scenario_ins in answer:
                clear()
                print(ROOM_DESIGN)
                type_delay(f"Where do you look?\n"
                f"Forward{Fore.BLUE}(NORTH){Fore.WHITE}, "
                f"To Your Right{Fore.GREEN}(East){Fore.WHITE}, "
                f"Behind You{Fore.RED}(South){Fore.WHITE} "
                f"or to Your Left{Fore.YELLOW}(West){Fore.WHITE}\n")
                look_answer = input("Answer: ").lower()
                # When the user look to the North
                north_scenario = "north"
                north_scenario_n = "n"
                north_scenario_for = "forward"
                north_scenario_str = "straight"
                north_scenario_ah = "ahead"
                # When the user look to the East
                east_scenario = "east"
                east_scenario = "e"
                east_scenario_r = "right"
                if north_scenario in look_answer or north_scenario_n in look_answer or north_scenario_for in look_answer or north_scenario_str in look_answer or north_scenario_ah in look_answer:
                    clear()
                    print(ROOM_DESIGN_NORTH)
                    type_delay(f"{Fore.BLUE}{look_answer}:{Fore.WHITE}" +
                    " You see a door… What do you do?\n")
                    north_answer = input("Answer: ").lower()
                    # When the player enter any of the following key words
                    door_scenario = "inspect"
                    door_scenario_app = "approach"
                    door_scenario_open = "open"
                    door_scenario_near = "near"
                    door_scenario_look = "look"
                    # When the user tries to move the bookshelf
                    move_bookshelf = "move"
                    move_bookshelf_push = "push"
                    # When the user inspect the door
                    if door_scenario in north_answer or door_scenario_app in north_answer or door_scenario_open in north_answer or door_scenario_near in north_answer or door_scenario_look in north_answer:
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
                                elif north_yes_input != 3012:
                                    print("Incurrect, try again")
                                elif north_yes_input in ("back", "quit"):
                                    break
                                elif int(north_yes_input) != int():
                                    print("Only numbers please")
                                else:
                                    print(wrong_input)
                            elif north_inspect_answer in ("n", "no"):
                                break
                    elif north_answer == "nothing":
                        print("You should at least do SOMETHING!")
                        return
                    else:
                        break
                # When the user looks east
                elif east_scenario in look_answer or east_scenario in look_answer or east_scenario_r in look_answer:
                    clear()
                    print(ROOM_DESIGN_EAST)
                    type_delay(f"{Fore.GREEN}{look_answer}:{Fore.WHITE}" +
                    "You Turn to your right and see a big bookshelf"
                    " that is almost as wide as the wall. "
                    "What do you do?\n")
                    east_answer = input("Answer: ").lower()
                    # When the user inspect the bookshelf
                    if door_scenario in east_answer or door_scenario_app in east_answer or door_scenario_near in east_answer or door_scenario_look in east_answer:
                        type_delay(STORY_EAST_INSPECT)
                        term_bookshelf= input("Answer: ").lower()
                        while True:
                            # When user inspect the purple book
                            term_bookshelf_purple = "purple"
                            # When user inspects the Red books
                            term_bookshelf_red = "red"
                            if door_scenario in term_bookshelf or door_scenario_app in term_bookshelf or door_scenario_look in term_bookshelf or door_scenario_open in term_bookshelf :
                                print("Which book do you look at?")
                                continue
                            elif term_bookshelf_purple in term_bookshelf:
                                print(INSPECT_BOOK_PURPLE)
                            elif term_bookshelf_red in term_bookshelf:
                                while True:
                                    print(INSPECT_BOOK_RED)
                                    red_book_inspect = input("Answer: ").lower()
                                    if red_book_inspect in ("y", "yes"):
                                        print(OPEN_RED_BOOK)
                                    elif red_book_inspect in ("n", "no"):
                                        print("You are facing the bookshelf again, What do you do now?")
                                    else:
                                        print(wrong_input)
                                        break
                            else:
                                break
                    elif move_bookshelf in east_answer or move_bookshelf_push in east_answer:
                        type_delay("You are not strong enough to do that...")
                        break
                    elif east_answer == "back":
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
            elif "nothing" in answer:
                print("You should at least try... otherwise, why are you playing the game?")
                break
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