"""
Start of the Project and File
"""
import os
from tkinter.tix import TEXT  # To clear the console
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
        if answer == "exit" or "quit" or "i want to leave" or "let me out":
            exit_app()
        

main_menu()