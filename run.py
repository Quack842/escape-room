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
# Starting scenarios
start_scenario = ["start", "begin", "let's go", "started", "wall", "anywhere"]
# Faceing right scenario
face_right = ["right", "look to my right", "look to the right"]
# Faceing right scenario
face_left = ["left", "look to my left", "look to the left"]
# Info scenarios
info_scenario = ["info", "information"]
# Default scenarios
first_scenario = ["look", "approach", "inspect", "walk",
"investigate", "forward", "anything", "go to", "move",
"around", "search"]
# Possible inputs for looking to the North
north_scenario = ["north", "forward", "straight", "ahead", "infront"]
# When the user look to the East
east_scenario = ["east", "right"]
# When the user look to the South
south_scenario = ["south", "behind", "backwards"]
# When the user look to the West
west_scenario = ["west", "left"]
# When the user quit or exit the game
exit_scenario = ["exit", "quit", "give up", "terminate", "kill code"]
# When the user wants to go back
back_scenario = ["back", "rewind", "step back"]
# When the player enter any of the following key words for open north door
door_scenario = ["inspect", "approach", "open", "near", "look", "break", "unlock"]
# When the user inspect the bookshelf
bookshelf_scenario = ["inspect", "approach", "closer", "take",
"open", "investigate", "read", "climb", "look"]
# When the user tries to move the bookshelf
move_scenario = ["move", "push", "shove"]
# When user inspect the purple book
term_purple_scenario = ["purple"]
# When user inspects the Red books
term_red_scenario = ["red"]
# Sticker scenario
purple_book_scenario = ["scratch", "knife"]
# South Scenario
south_scenario_inpsect = ["approach", "inspect", "climb", "kick", "investigate", "go to"]
# Scenarios for Desk
desk_scenario = ["approach", "inspect", "go to", "open"]
# Possible yes anwers
north_inspect_scenario = ["y", "yes", "indeed", "of course", "ofcourse"]
# Possible Death anwers
death_scenario = ["die", "kill myself", "end myself", "cut myself", "off myself", "suicide"]
# Life Tips random array
tips_list = [TIPS_1, TIPS_2, TIPS_3, TIPS_4, TIPS_5, TIPS_6, TIPS_7, TIPS_8, TIPS_9, TIPS_10]
# Hints random array
hints_list = [HINT_1, HINT_2, HINT_3, HINT_4, HINT_5, HINT_6, HINT_7]

def main_menu():
    """
    This will be the landing, the user will first see this page before entering the game.
    """
    clear()
    print(TITLE)
    print(MAIN_TEXT)
    while True:
        answer = input(
            f"To start the game, type {Fore.BLUE}start{Fore.WHITE}. "
            f"If you want to know more about the game and how to play this game"
            f"type {Fore.BLUE}Info/Information{Fore.WHITE} "
            f"Whenever you want to exit the app, just type {Fore.BLUE}kill code{Fore.WHITE}\n" +
            "Answer: "
        ).lower()
        if any(x in answer for x in start_scenario) or answer == "s":
            start_game()
        elif any(x in answer for x in exit_scenario):
            exit_app()
        elif any(x in answer for x in info_scenario) or answer == "i":
            information_menu()
        else:
            type_delay(INVALID_COMMAND)

def get_username():
    """
    This function will retreive the username that the user will enter.
    """
    while True:
        name = input("What should I call you?\n" + "Answer: ").strip()
        if len(name) < 2:
            clear()
            print(f"{Fore.RED}The Length of the username is too short,"
            f" please try again{Fore.WHITE}")
        elif len(name) > 15:
            clear()
            print(f"{Fore.RED}The username is too long, try a shorter username.{Fore.WHITE}")
        elif any(char.isdigit() for char in name):
            clear()
            print(f"{Fore.RED}The username cannot contain any numbers.{Fore.WHITE}")
        elif all(char.isalpha() or char.isspace() for char in name):
            global USERNAME
            USERNAME = " ".join(name.split()).title()
            break
        else:
            clear()
            print(f"{Fore.RED}Your name cannot contain any symbols, please try again.{Fore.WHITE}")

def start_game():
    """
    When the user answers 'start' this function will run and the user
    can start playing the game.
    """
    clear()
    type_delay("Game is starting.")
    type_delay(".")
    type_delay(".\n")
    get_username()

    type_delay(random.choice(random.choice(tips_list)))
    print(ROOM_DESIGN)
    landing_start()

def landing_start():
    """
    When the user want to come back to this scene
    """
    type_delay("Well hello, " + USERNAME)
    while True:
        type_delay(STORY_START + USERNAME + "?\n")
        answer = input("Answer: ").lower()
        if any(x in answer for x in first_scenario):
            clear()
            print(ROOM_DESIGN)
            type_delay(f"Where do you look?\n"
            f"Forward{Fore.BLUE}(NORTH){Fore.WHITE}, "
            f"To Your Right{Fore.GREEN}(East){Fore.WHITE}, "
            f"Behind You{Fore.RED}(South){Fore.WHITE} "
            f"or to Your Left{Fore.YELLOW}(West){Fore.WHITE}\n")
            while True:
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
                elif any(x in look_answer for x in death_scenario):
                    print(SUICIDE_TEXT)
                    type_delay("Ireland suicide Helpline: 1800 247 247")
                elif "up" in look_answer:
                    type_delay("You look up... there is a single light bulb flickering above you. ")
                elif "down" in look_answer:
                    type_delay("You look down... you're looking at your feet..."
                    " I wonder if you'll use them. ")
                elif "kick" in look_answer:
                    type_delay("Why would you kick?... What would you kick?"
                    " What will this achieve?... Do anything else")
                    Event().wait(2)
                elif "kill code" in answer:
                    exit_app()
                elif "tip" in answer:
                    type_delay(random.choice(tips_list))
                elif "hint" in answer:
                    type_delay(random.choice(hints_list))
                else:
                    type_delay(INVALID_COMMAND)
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
        elif "kill code" in answer:
            exit_app()
        elif "tip" in answer:
            type_delay(random.choice(tips_list))
        elif "hint" in answer:
            type_delay(random.choice(hints_list))
        else:
            type_delay(INVALID_COMMAND)

def north_face(look_answer):
    """
    When the user looks north, the following function will execute.
    """
    clear()
    print(ROOM_DESIGN_NORTH)
    while True:
        type_delay(f"{Fore.BLUE}{look_answer}:{Fore.WHITE}" +
        f" You see a door… What do you do {USERNAME}?\n")
        north_answer = input("Answer: ").lower()
        # When the user inspect the door
        if any(x in north_answer for x in door_scenario):
            while True:
                type_delay(STORY_NORTH_INSPECT)
                north_inspect_answer = input("Answer: ").lower()
                if any(x in north_inspect_answer for x in north_inspect_scenario):
                    while True:
                        north_yes_input = input("Please enter the 4 digit code ('back' to return): ")
                        if north_yes_input == str(3012):
                            type_delay("You entered the \033[5;35m4\033[0;0m digit code,"
                            " you fiddle with the lock and"
                            " all of a sudden *CLICK*. You unlocked the door!")
                            Event().wait(1)
                            animate_rocket()
                        elif len(north_yes_input) < 4:
                            print(f"{Fore.RED}Invalid:{Fore.WHITE} It is a \033[5;35m4\033[0;0m digit combination lock,"
                            f" you entered {Fore.BLUE}{north_yes_input}{Fore.WHITE}\n."
                            f" That is {Fore.BLUE}{len(north_yes_input)}{Fore.WHITE} digits,"
                            " you need to enter a 4 digit code.\n")
                        elif len(north_yes_input) > 4:
                            print(f"{Fore.RED}Invalid:{Fore.WHITE} It is a 4 digit combination lock,"
                            f" you entered {Fore.BLUE}{north_yes_input}{Fore.WHITE}."
                            f" That is {Fore.BLUE}{len(north_yes_input)}{Fore.WHITE} digits, you need"
                            " to enter a 4 digit code.\n")
                        elif not north_yes_input.isnumeric():
                            print(f"{Fore.RED}Only numbers please{Fore.WHITE}\n")
                        elif any(x in north_yes_input for x in back_scenario):
                            clear()
                            type_delay("Going Back.")
                            type_delay(".")
                            type_delay(".")
                            Event().wait(1)
                            break
                        elif north_yes_input != "3012":
                            print(f"{Fore.RED}Incorrect{Fore.WHITE}, try again\n")
                        elif "kill code" in north_yes_input:
                            exit_app()
                        elif "tip" in north_yes_input:
                            type_delay(random.choice(tips_list))
                        elif "hint" in north_yes_input:
                            type_delay(random.choice(hints_list))
                        else:
                            type_delay(INVALID_COMMAND)
                elif north_inspect_answer in ("n", "no"):
                    break
                elif "kill code" in north_inspect_answer:
                    exit_app()
                elif "tip" in north_inspect_answer:
                    type_delay(random.choice(tips_list))
                elif "hint" in north_inspect_answer:
                    type_delay(random.choice(hints_list))
                else:
                    type_delay(INVALID_COMMAND)
        elif north_answer == "nothing":
            print("You should at least do SOMETHING!")
        elif "kick" in north_answer:
            type_delay("Please don't kick my door... Thats rude, now you have to wait"
            " 3 seconds...\n")
            Event().wait(3)
        elif any(x in north_answer for x in face_left):
            west_face(look_answer)
        elif any(x in north_answer for x in face_right):
            east_face(look_answer)
        elif any(x in north_answer for x in back_scenario):
            landing_start()
        elif any(x in north_answer for x in east_scenario):
            east_face(look_answer)
        elif any(x in north_answer for x in south_scenario):
            south_face(look_answer)
        elif any(x in north_answer for x in west_scenario):
            west_face(look_answer)
        elif "kill code" in north_answer:
            exit_app()
        elif "tip" in north_answer:
            type_delay(random.choice(tips_list))
        elif "hint" in north_answer:
            type_delay(random.choice(hints_list))
        else:
            type_delay(INVALID_COMMAND)

def east_face(look_answer):
    """
    When the user look to the east.
    """
    clear()
    print(ROOM_DESIGN_EAST)
    while True:
        type_delay(f"{Fore.GREEN}{look_answer}: {Fore.WHITE}" +
        "You turn to your right and see a big bookshelf"
        " that is almost as wide as the wall. "
        f"What do you do {USERNAME}?\n")
        east_answer = input("Answer: ").lower()
        if any(x in east_answer for x in bookshelf_scenario):
            while True:
                type_delay(STORY_EAST_INSPECT)
                term_bookshelf= input("Answer: ").lower()
                if any(x in term_bookshelf for x in term_purple_scenario):
                    type_delay(INSPECT_BOOK_PURPLE + USERNAME + "?\n")
                    purple_book_answer = input("Answer: ").lower()
                    if "scratch" in purple_book_answer:
                        while True:
                            print("With what do you scratch it with?")
                            scratch_answer = input("Asnwer: ").lower()
                            if "knife" in scratch_answer:
                                print(f"You scratched the sticker off and it"
                                f" reavealed the number {Fore.LIGHTYELLOW_EX}1{Fore.WHITE}")
                            elif "nail" in scratch_answer:
                                type_delay("As you try to scratch off this sticker of a duck, you break your nail...\n")
                                Event().wait(2)
                            elif "back" in scratch_answer:
                                break
                            elif "kill code" in scratch_answer:
                                exit_app()
                            elif "tip" in scratch_answer:
                                type_delay(random.choice(tips_list))
                            elif "hint" in scratch_answer:
                                type_delay(random.choice(hints_list))
                            else:
                                type_delay(INVALID_COMMAND)
                    elif "search" in purple_book_answer:
                        type_delay(SEARCH_COMMAND)
                    elif "kill code" in purple_book_answer:
                        exit_app()
                    elif "tip" in purple_book_answer:
                        type_delay(random.choice(tips_list))
                    elif "hint" in purple_book_answer:
                        type_delay(random.choice(hints_list))
                    else:
                        type_delay(INVALID_COMMAND)
                elif any(x in term_bookshelf for x in term_red_scenario):
                    while True:
                        type_delay(INSPECT_BOOK_RED)
                        red_book_inspect = input("Answer: ").lower()
                        if red_book_inspect in ("y", "yes"):
                            type_delay(OPEN_RED_BOOK)
                            Event().wait(2)
                            clear()
                            break
                        elif red_book_inspect in ("n", "no"):
                            type_delay("You get the feeling that you just saved 2 hours")
                            Event().wait(1)
                            break
                        elif "kill code" in red_book_inspect:
                            exit_app()
                        elif "tip" in red_book_inspect:
                            type_delay(random.choice(tips_list))
                        elif "hint" in red_book_inspect:
                            type_delay(random.choice(hints_list))
                        else:
                            type_delay(INVALID_COMMAND)
                            break
                elif any(x in term_bookshelf for x in face_left):
                    north_face(look_answer)
                elif any(x in term_bookshelf for x in face_right):
                    south_face(look_answer)
                elif any(x in term_bookshelf for x in back_scenario):
                    landing_start()
                elif any(x in term_bookshelf for x in north_scenario):
                    north_face(look_answer)
                elif any(x in term_bookshelf for x in south_scenario):
                    south_face(look_answer)
                elif any(x in term_bookshelf for x in west_scenario):
                    west_face(look_answer)
                elif "kill code" in term_bookshelf:
                    exit_app()
                elif "tip" in term_bookshelf:
                    type_delay(random.choice(tips_list))
                elif "hint" in term_bookshelf:
                    type_delay(random.choice(hints_list))
                else:
                    type_delay(INVALID_COMMAND)
        elif any(x in east_answer for x in move_scenario):
            type_delay("You are not strong enough to do that...\n")
            Event().wait(2)
        elif any(x in east_answer for x in face_left):
            north_face(look_answer)
        elif any(x in east_answer for x in face_right):
            south_face(look_answer)
        elif any(x in east_answer for x in back_scenario):
            landing_start()
        elif any(x in east_answer for x in north_scenario):
            north_face(look_answer)
        elif any(x in east_answer for x in south_scenario):
            south_face(look_answer)
        elif any(x in east_answer for x in west_scenario):
            west_face(look_answer)
        elif "kill code" in east_answer:
            exit_app()
        elif "tip" in east_answer:
            type_delay(random.choice(tips_list))
        elif "hint" in east_answer:
            type_delay(random.choice(hints_list))
        else:
            type_delay(INVALID_COMMAND)

def south_face(look_answer):
    """
    When the user Looks to the south
    """
    clear()
    print(ROOM_DESIGN_SOUTH)
    while True:
        type_delay(f"{Fore.RED}{look_answer}: {Fore.WHITE}" +
        f"You See a table with two chairs on each side. What do you do {USERNAME}?\n")
        south_scenario_answer = input("Answer: ").lower()
        if any(x in south_scenario_answer for x in south_scenario_inpsect):
            type_delay(INSPECT_CHAIRS)
            Event().wait(1)
        elif "sit" in south_scenario_answer:
            type_delay(SIT_CHAIRS)
            Event().wait(3)
        elif "stand" in south_scenario_answer:
            type_delay(STAND_CHAIR)
            Event().wait(3)
        elif any(x in south_scenario_answer for x in back_scenario):
            break
        elif any(x in south_scenario_answer for x in death_scenario):
            print(SUICIDE_TEXT)
            type_delay("Ireland suicide Helpline: 1800 247 247")
        elif any(x in south_scenario_answer for x in face_left):
            east_face(look_answer)
        elif any(x in south_scenario_answer for x in face_right):
            west_face(look_answer)
        elif any(x in south_scenario_answer for x in north_scenario):
            north_face(look_answer)
        elif any(x in south_scenario_answer for x in east_scenario):
            east_face(look_answer)
        elif any(x in south_scenario_answer for x in west_scenario):
            west_face(look_answer)
        elif "kill code" in south_scenario_answer:
            exit_app()
        elif "tip" in south_scenario_answer:
            type_delay(random.choice(tips_list))
        elif "hint" in south_scenario_answer:
            type_delay(random.choice(hints_list))
        else:
            type_delay(INVALID_COMMAND)

def west_face(look_answer):
    """
    When the user faces the west side
    """
    clear()
    print(ROOM_DESIGN_WEST)
    while True:
        type_delay(f"{Fore.YELLOW}{look_answer}: {Fore.WHITE}" +
        f"You turn to your left, you see a desk. What do you do {USERNAME}?\n")
        desk_answer = input("Answer: ").lower()
        if any(x in desk_answer for x in desk_scenario):
            type_delay(DESK_INPSECT + USERNAME + "?\n")
            desk_scenario_answer = input("Answer: ").lower()
            if "take" in desk_scenario_answer:
                type_delay("You take the Knife.")
                type_delay(".")
                type_delay(".\n")
                Event().wait(1)
            elif "open" in desk_scenario_answer:
                type_delay("Which one do you open?\n")
                desk_open_scenario = input("Answer: ").lower()
                if "left" in desk_open_scenario:
                    type_delay(LEFT_DRAWER)
                    Event().wait(2)
                elif "right" in desk_open_scenario:
                    type_delay(LEFT_DRAWER)
                    Event().wait(2)
                elif "kill code" in desk_open_scenario:
                    exit_app()
                elif "tip" in desk_open_scenario:
                    type_delay(random.choice(tips_list))
                elif "hint" in desk_open_scenario:
                    type_delay(random.choice(hints_list))
                else:
                    type_delay(INVALID_COMMAND)
            elif "kill code" in desk_scenario_answer:
                exit_app()
            elif "tip" in desk_scenario_answer:
                type_delay(random.choice(tips_list))
            elif "hint" in desk_scenario_answer:
                type_delay(random.choice(hints_list))
            else:
                type_delay(INVALID_COMMAND)
        elif any(x in desk_answer for x in back_scenario):
            break
        elif any(x in desk_answer for x in death_scenario):
            print(SUICIDE_TEXT)
            type_delay("Ireland suicide Helpline: 1800 247 247")
        elif any(x in desk_answer for x in face_left):
            south_face(look_answer)
        elif any(x in desk_answer for x in face_right):
            north_face(look_answer)
        elif any(x in desk_answer for x in north_scenario):
            north_face(look_answer)
        elif any(x in desk_answer for x in south_scenario):
            south_face(look_answer)
        elif any(x in desk_answer for x in east_scenario):
            east_face(look_answer)
        elif "kill code" in desk_answer:
            exit_app()
        elif "tip" in desk_answer:
            type_delay(random.choice(tips_list))
        elif "hint" in desk_answer:
            type_delay(random.choice(hints_list))
        else:
            type_delay(INVALID_COMMAND)

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
    type_delay("\nAre you positive you want to quit the app?\n")
    while True:
        exit_answer = input(
            f"Type {Fore.BLUE}Y{Fore.WHITE} if you want to quit the app "
            f"or type {Fore.BLUE}N{Fore.WHITE} if you want to stay and try again.\n"
        )
        if "y" in exit_answer:
            print(GOODBYE)
            type_delay("Closing the application... Have a Nice day!")
            quit()
        elif "n" in exit_answer:
            main_menu()
        else:
            type_delay(INVALID_COMMAND)

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

def information_menu():
    """
    The details on how to play the game will be displayed.
    """
    clear()
    print(INFORMATION_TEXT)
#FINISHED animation
def animate_rocket():
    """
    when the user finshed the game this animation will display
    """
    distance_from_top = 20
    while True:
        print("\n" * distance_from_top)
        print(f"     {Fore.BLUE}.{Fore.WHITE}    /\             {Fore.RED}.{Fore.WHITE}    /\             {Fore.BLUE}.{Fore.WHITE}    /\   {Fore.BLUE}.{Fore.WHITE}        {Fore.RED}.{Fore.WHITE}    /\ ")
        print(f" {Fore.GREEN}.{Fore.WHITE}     {Fore.YELLOW}.{Fore.WHITE}  ||        {Fore.YELLOW}.{Fore.WHITE}         ||   {Fore.YELLOW}.{Fore.WHITE}    {Fore.GREEN}.{Fore.WHITE}         ||     {Fore.BLUE}.{Fore.WHITE}   {Fore.GREEN}.{Fore.WHITE}    {Fore.YELLOW}.{Fore.WHITE}  ||")
        print(f"   {Fore.BLUE}.{Fore.WHITE}   {Fore.GREEN}.{Fore.WHITE}  ||      {Fore.GREEN}.{Fore.WHITE}           ||      {Fore.RED}.{Fore.WHITE}     {Fore.BLUE}.{Fore.WHITE}     ||   {Fore.YELLOW}.{Fore.WHITE}      {Fore.RED}.{Fore.WHITE}   {Fore.BLUE}.{Fore.WHITE}  ||")
        print(f"     {Fore.RED}.{Fore.WHITE}   /||\          {Fore.BLUE}.{Fore.WHITE}     /||\       {Fore.RED}.{Fore.WHITE}        /||\    {Fore.YELLOW}.{Fore.WHITE}      {Fore.GREEN}.{Fore.WHITE}   /||\ ")

        time.sleep(0.1)
        os.system('clear')
        distance_from_top -= 1
        if distance_from_top < 0:
            distance_from_top = 20

            clear()
            print(ESCAPED_MSG)
            input("Press Enter to continue...")
            main_menu()

main_menu()
