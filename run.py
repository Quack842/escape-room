"""
Start of the Project and File
"""
import os
import sys
import random
from threading import Event
import time  # To give a delay when typing
import colorama # Import Colors into project
from colorama import Fore
from text import *
colorama.init()

#Global Var for the username, age and location
USERNAME = ""
# Default scenarios
first_scenario = ["look", "approach", "inspect", "walk", "investigate", "forward"]
# Possible inputs for looking to the North
north_scenario = ["north", "forward", "straight", "ahead", "infront"]
# When the user look to the East
east_scenario = ["east", "right"]
# When the user look to the South
south_scenario = ["south", "behind", "backwards"]
# When the user look to the West
west_scenario = ["west", "left"]
# When the user quit or exit the game
exit_scenario = ["exit", "quit", "give up", "terminate"]
# When the user wants to go back
back_scenario = ["back", "rewind", "step back"]
# When the player enter any of the following key words for open north door
door_scenario = ["inspect", "approach", "open", "near", "look", "break", "unlock"]
# When the user inspect the bookshelf
bookshelf_scenario = ["inspect", "approach", "closer", "take",
"open", "investigate", "read", "climb"]
# When the user tries to move the bookshelf
move_scenario = ["move", "push", "shove"]
# When user inspect the purple book
term_purple_scenario = ["purple"]
# When user inspects the Red books
term_red_scenario = ["red"]
# Sticker scenario
purple_book_scenario = ["scratch", "knife"]
# South Scenario
south_scenario_inpsect = ["approach", "inspect", "climb", "kick", "investigate"]
# Scenarios for Desk
desk_scenario = ["approach", "inspect"]
# Possible yes anwers
north_inspect_scenario = ["y", "yes", "indeed", "of course", "ofcourse"]
# Possible Death anwers
death_scenario = ["die", "kill myself", "end myself", "cut myself", "off myself", "suicide"]

def main_menu():
    """
    This will be the landing, the user will first see this page before entering the game.
    """
    clear()
    print(TITLE)
    print(MAIN_TEXT)
    print(random.choices(TIPS_1,TIPS_2))

    while True:
        answer = input(
            f"To start The game, type {Fore.BLUE}start{Fore.WHITE}. "
            f"If you want to know more about the game and how to play this game"
            f"type {Fore.BLUE}Info/Information{Fore.WHITE} "
            f"If you want to exit the application, just type {Fore.BLUE}exit{Fore.WHITE}\n" +
            "Answer: "
        ).lower()
        if answer in ("start", "strt"):
            start_game()
        elif answer in ("exit"):
            exit_app()
        elif answer in ("info", "information", "i"):
            information_menu()
        else:
            type_delay(wrong_input())

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
    landing_start()

def landing_start():
    """
    When the user want to come back to this scene
    """
    type_delay(USERNAME)
    type_delay(STORY_START)
    answer = input("Answer: ").lower()
    while True:
        if any(x in answer for x in first_scenario):
            clear()
            print(ROOM_DESIGN)
            type_delay(f"Where do you look?\n"
            f"Forward{Fore.BLUE}(NORTH){Fore.WHITE}, "
            f"To Your Right{Fore.GREEN}(East){Fore.WHITE}, "
            f"Behind You{Fore.RED}(South){Fore.WHITE} "
            f"or to Your Left{Fore.YELLOW}(West){Fore.WHITE}\n")
            look_answer = input("Answer: ").lower()
            if any(x in look_answer for x in north_scenario) or look_answer == "n":
                north_face(look_answer)
            # When the user looks east
            elif any(x in look_answer for x in east_scenario) or look_answer == "e":
                east_face(look_answer)
            # When the user look to the South
            elif any(x in look_answer for x in south_scenario) or look_answer == "s":
                south_face(look_answer)
            # When the user look to the West
            elif any(x in look_answer for x in west_scenario) or look_answer == "w":
                west_face(look_answer)
            # When the user want to exit
            elif any(x in look_answer for x in exit_scenario):
                exit_app()
            # When the user lwant to go back
            elif any(x in look_answer for x in back_scenario):
                landing_start()
            elif "up" in look_answer:
                type_delay("You look up... there is a single light bulb flickering above you. ")
            elif "down" in look_answer:
                type_delay("You look down... you're looking at your feet..."
                " I wonder if you'll use them. ")
            else:
                type_delay(wrong_input())
                landing_start()
        elif "nothing" in answer:
            type_delay("You should at least try... otherwise, why are you playing the game?")
        elif any(x in answer for x in back_scenario):
            landing_start()
        elif any(x in answer for x in death_scenario):
            clear()
            print(SUICIDE_TEXT)
            type_delay("Ireland suicide Helpline: 1800 247 247")
            Event().wait(3)
            clear()
            landing_start()
        else:
            type_delay(wrong_input())
            landing_start()

def north_face(look_answer):
    """
    When the user looks north, the following function will execute.
    """
    clear()
    print(ROOM_DESIGN_NORTH)
    type_delay(f"{Fore.BLUE}{look_answer}:{Fore.WHITE}" +
    " You see a door… What do you do?\n")
    north_answer = input("Answer: ").lower()
    # When the user inspect the door
    if any(x in north_answer for x in door_scenario):
        type_delay(STORY_NORTH_INSPECT)
        north_inspect_answer = input("Answer: ").lower()
        while True:
            if any(x in north_inspect_answer for x in north_inspect_scenario):
                north_yes_input = input("Please enter the 4 digit code ('back' to return): ")
                #while True:
                if north_yes_input == str(3012):
                    type_delay("You entered the \033[5;35m4\033[0;0m digit code,"
                    " you fiddle with the lock and"
                    " all of a sudden *CLICK*. You unlocked the door!")
                    clear()
                    print(ESCAPED_MSG)
                    input("Press Enter to continue...")
                    main_menu()
                elif len(north_yes_input) < 4:
                    print(f"It is a \033[5;35m4\033[0;0m digit combination lock,"
                    f" you entered {Fore.BLUE}{north_yes_input}{Fore.WHITE}."
                    f" That is {Fore.BLUE}{len(north_yes_input)}{Fore.WHITE} digits,"
                    " you need to enter a 4 digit code.")
                elif len(north_yes_input) > 4:
                    print(f"It is a 4 digit combination lock,"
                    f" you entered {Fore.BLUE}{north_yes_input}{Fore.WHITE}."
                    f" That is {Fore.BLUE}{len(north_yes_input)}{Fore.WHITE} digits, you need"
                    " to enter a 4 digit code.")
                elif any(x in north_yes_input for x in back_scenario):
                    clear()
                    type_delay("Going Back...")
                    type_delay("..")
                    type_delay(".")
                    Event().wait(1)
                    landing_start()
                elif not north_yes_input.isnumeric():
                    print("Only numbers please")
                elif north_yes_input != "3012":
                    print(f"{Fore.RED}Incorrect{Fore.WHITE}, try again")
                else:
                    type_delay(wrong_input())
            elif north_inspect_answer in ("n", "no"):
                landing_start()
    elif north_answer == "nothing":
        print("You should at least do SOMETHING!")
        return
    elif any(x in north_answer for x in back_scenario):
        landing_start()
    elif any(x in north_answer for x in east_scenario):
        east_face(look_answer)
    elif any(x in north_answer for x in south_scenario):
        south_face(look_answer)
    elif any(x in north_answer for x in west_scenario):
        west_face(look_answer)
    else:
        type_delay(wrong_input())

def east_face(look_answer):
    """
    When the user look to the east.
    """
    clear()
    print(ROOM_DESIGN_EAST)
    type_delay(f"{Fore.GREEN}{look_answer}: {Fore.WHITE}" +
    "You Turn to your right and see a big bookshelf"
    " that is almost as wide as the wall. "
    "What do you do?\n")
    east_answer = input("Answer: ").lower()
    if any(x in east_answer for x in bookshelf_scenario):
        type_delay(STORY_EAST_INSPECT)
        term_bookshelf= input("Answer: ").lower()
        if any(x in term_bookshelf for x in term_purple_scenario):
            type_delay(INSPECT_BOOK_PURPLE)
            purple_book_answer = input("Answer: ").lower()
            if "scratch" in purple_book_answer:
                while True:
                    print("With what do you scratch it with?")
                    scratch_answer = input("Asnwer: ").lower()
                    if "knife" in scratch_answer:
                        print(f"You scratched the sticker off and it"
                        f" reavealed the number {Fore.LIGHTYELLOW_EX}1{Fore.WHITE}")
                        break
                    elif "nail" in scratch_answer:
                        print("That wont work...")
                        break
                    else:
                        type_delay(wrong_input())
                        break
            else:
                type_delay(wrong_input())
        elif any(x in term_bookshelf for x in term_red_scenario):
            type_delay(INSPECT_BOOK_RED)
            red_book_inspect = input("Answer: ").lower()
            while True:
                if red_book_inspect in ("y", "yes"):
                    type_delay(OPEN_RED_BOOK)
                    Event().wait(2)
                    east_face(look_answer)
                elif red_book_inspect in ("n", "no"):
                    print("You get the feeling that you just saved 2 hours")
                    east_face(look_answer)
                else:
                    type_delay(wrong_input())
                    east_face(look_answer)
        else:
            type_delay(wrong_input())
            east_face(look_answer)
    elif any(x in east_answer for x in move_scenario):
        type_delay("You are not strong enough to do that...")
        east_face(look_answer)
    elif any(x in east_answer for x in back_scenario):
        landing_start()
    elif any(x in east_answer for x in north_scenario):
        north_face(look_answer)
    elif any(x in east_answer for x in south_scenario):
        south_face(look_answer)
    elif any(x in east_answer for x in west_scenario):
        west_face(look_answer)
    else:
        type_delay(wrong_input())

def south_face(look_answer):
    """
    When the user Looks to the south
    """
    clear()
    print(ROOM_DESIGN_SOUTH)
    type_delay(f"{Fore.RED}{look_answer}: {Fore.WHITE}" +
    "You See a table with two chairs on each side. What do you do?\n")
    south_scenario_answer = input("Answer: ").lower()
    loop_var = False
    while not loop_var:
        if any(x in south_scenario_answer for x in south_scenario_inpsect):
            # loop_var = True
            print(INSPECT_CHAIRS)
            Event().wait(3)
            south_face(look_answer)
        elif "sit" in south_scenario_answer:
            #loop_var = True
            type_delay(SIT_CHAIRS)
            Event().wait(3)
            south_face(look_answer)
        elif "stand" in south_scenario_answer:
            #loop_var = True
            type_delay(STAND_CHAIR)
            Event().wait(3)
            south_face(look_answer)
        elif any(x in south_scenario_answer for x in back_scenario):
            #oop_var = True
            landing_start()
        elif any(x in south_scenario_answer for x in north_scenario):
            #loop_var = True
            north_face(look_answer)
        elif any(x in south_scenario_answer for x in east_scenario):
            #loop_var = True
            east_face(look_answer)
        elif any(x in south_scenario_answer for x in west_scenario):
            #oop_var = True
            west_face(look_answer)
        else:
            type_delay(wrong_input())
            south_face(look_answer)

def west_face(look_answer):
    """
    When the user faces the west side
    """
    clear()
    print(ROOM_DESIGN_WEST)
    type_delay(f"{Fore.YELLOW}{look_answer}: {Fore.WHITE}" +
    "You turn to your left, you see a desk. What do you do?\n")
    desk_answer = input("Answer: ").lower()
    if any(x in desk_answer for x in desk_scenario):
        type_delay(DESK_INPSECT)
        desk_scenario_answer = input("Answer: ").lower()
        if "take" in desk_scenario_answer:
            type_delay("You take the Knife")
            Event().wait(1)
            west_face(look_answer)
        elif "open" in desk_scenario_answer:
            print("Which one do you open?\n")
            desk_open_scenario = input("Answer: ").lower()
            if "left" in desk_open_scenario:
                type_delay(LEFT_DRAWER)
                Event().wait(3)
                west_face(look_answer)
            elif "right" in desk_open_scenario:
                type_delay(LEFT_DRAWER)
                Event().wait(3)
                west_face(look_answer)
    elif any(x in desk_answer for x in back_scenario):
        landing_start()
    elif any(x in desk_answer for x in north_scenario):
        north_face(look_answer)
    elif any(x in desk_answer for x in south_scenario):
        south_face(look_answer)
    elif any(x in desk_answer for x in east_scenario):
        east_face(look_answer)

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
            type_delay(wrong_input())

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

def wrong_input():
    """
    When the user enters an invalid
    """
    print(f"{Fore.RED}Invalid command{Fore.WHITE}, please make sure of spelling and try again")

def information_menu():
    """
    The details on how to play the game will be displayed.
    """
    clear()
    print(INFORMATION_TEXT)

main_menu()
