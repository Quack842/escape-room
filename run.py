"""
Start of the Project and File
"""
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
        if answer == "Start" or answer == "start" or answer == "START":
            start_game()
        elif answer == "exit" or answer == "EXIT" or answer == "Exit":
            exit_app()
        elif answer == "info" or answer == "information" or answer == "Info" or answer == "Information":
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
        # MULTIPLE TERMS AS KBROTHER WHEN HE COMES BACK
        # MULTIPLE TERMS AS KBROTHER WHEN HE COMES BACK
        # MULTIPLE TERMS AS KBROTHER WHEN HE COMES BACK
        # MULTIPLE TERMS AS KBROTHER WHEN HE COMES BACK
        term = "look"
        answer = input("Answer: ").lower()
        words = answer.split()

        if term in words:
            type_delay(f"Where do you look first?\n"
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
                north_answer = input("Asnwer: ").lower()
                # MULTIPLE TERMS AS KBROTHER WHEN HE COMES BACK
                # MULTIPLE TERMS AS KBROTHER WHEN HE COMES BACK
                # MULTIPLE TERMS AS KBROTHER WHEN HE COMES BACK
                # MULTIPLE TERMS AS KBROTHER WHEN HE COMES BACK

                # When the user inspect the door
                term_door = "inspect"
                words_inspect = north_answer.split()
                term_door_approach = "approach"
                words_approach = north_answer.split()
                term_door_open = "open"
                words_open = north_answer.split()
                if  term_door in words_inspect:
                    type_delay(STORY_NORTH_INSPECT)
                    
                # When the user approach the door
                elif term_door_approach in words_approach:
                    type_delay(STORY_NORTH_APPROACH)
                # When the user open the door
                elif term_door_open in words_open:
                    type_delay(STORY_NORTH_OPEN)
                elif north_answer == "back":
                    print(start_game)
                else:
                    print(wrong_input)

            # When the user look to the East
            elif look_answer in ("east", "e", "right"):
                clear()
                print(ROOM_DESIGN_EAST)
                type_delay(f"{Fore.GREEN}{look_answer}:{Fore.WHITE}" +
                "You Turn to your right and see a big bookshelf that is almost as wide as the wall. "
                "What do you do?\n")
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
            else:
                print(wrong_input)
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
            f"Type {Fore.BLUE}yes/YES/Y{Fore.WHITE} if you want to quit the app "
            f"or type {Fore.BLUE}no/NO/N{Fore.WHITE} if you want to stay and try again.\n"
        )
        if answer == "yes" or "YES" or "Y" or "y":
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
        time.sleep(.05)
    time.sleep(1)

def wrong_input(answer):
    """
    When the user gives an invalid input, the function will be called
    """
    print(f"\t{Fore.RED}Wrong command: {Fore.WHITE}'{answer}' is not a valid command."
    f"Please try again.\n"
    )

def information_menu():
    """
    The details on how to play the game will be displayed.
    """
    clear()
    print(INFORMATION_TEXT)


main_menu()