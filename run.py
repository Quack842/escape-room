"""
Start of the Project and File
"""
import imp
import os
from tkinter.tix import TEXT  # To clear the console
import datetime  # To get the hour of the day
import time  # To give a delay when typing
import colorama # Import Colors into project
from colorama import Fore
from text import *
colorama.init()

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
            f"type {Fore.BLUE} Info/Information{Fore.WHITE} "
            f"If you want to exit the application, just type {Fore.BLUE}exit{Fore.WHITE} "
        )
        if answer == "exit" or "i want to leave" or "let me out":
            exit_app()
        elif answer == "info" or "information":
            information_menu()

#Helper Functions
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
        system.stdout.write(char)
        system.stdout.flush()
        time.sleep(.2)
    time.sleep(3)

def wrong_input(answer):
    """
    When the user gives an invalid input, the function will be called
    """
    print(f"\t{Fore.RED}Wrong command: {Fore.WHITE}'{answer}'"
    f"Please enter a valid command.\n"
    )

def information_menu():
    """
    
    """
main_menu()