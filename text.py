"""
Start of the Project and File
"""
import os
import colorama
from colorama import Fore
colorama.init()

TITLE = """
______________________________________________________________________________________________

███████╗███████╗ ██████╗ █████╗ ██████╗ ███████╗    ██████╗  ██████╗  ██████╗ ███╗   ███╗
██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝    ██╔══██╗██╔═══██╗██╔═══██╗████╗ ████║
█████╗  ███████╗██║     ███████║██████╔╝█████╗      ██████╔╝██║   ██║██║   ██║██╔████╔██║
██╔══╝  ╚════██║██║     ██╔══██║██╔═══╝ ██╔══╝      ██╔══██╗██║   ██║██║   ██║██║╚██╔╝██║
███████╗███████║╚██████╗██║  ██║██║     ███████╗    ██║  ██║╚██████╔╝╚██████╔╝██║ ╚═╝ ██║
╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚══════╝    ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝
______________________________________________________________________________________________                                                                                        
"""

ROOM_DESIGN = f"""
 ________________________________________
|             |___________|              |
|                                        |
|                                     ___|
|                                    |   |
|  _____                             |   |
| |     |           {Fore.BLUE}N{Fore.WHITE}                |   |
| |     |         {Fore.YELLOW}W{Fore.WHITE} + {Fore.GREEN}E{Fore.WHITE}              |   |
| |     |           {Fore.RED}S{Fore.WHITE}                |   |
| |_____|                            |   |
|                                    |   |
|                                    |   |
|               __________           |   |
|              |          |          |   |
|           |  |          |  |       |___|
|           |  |          |  |           |
|______________|__________|______________|
"""

ROOM_DESIGN_NORTH = f"""
{Fore.BLUE}
 ________________________________________
|             |___________|              |
|                                        |
|                                     ___| {Fore.WHITE}
|                                    |   |
|  _____                             |   |
| |     |           {Fore.BLUE}N{Fore.WHITE}                |   |
| |     |         W + E              |   |
| |     |           S                |   |
| |_____|                            |   |
|                                    |   |
|                                    |   |
|               __________           |   |
|              |          |          |   |
|           |  |          |  |       |___|
|           |  |          |  |           |
|______________|__________|______________|
"""

ROOM_DESIGN_EAST = f"""
 _____________________________________{Fore.GREEN}___{Fore.WHITE}
|             |___________|          {Fore.GREEN}    |{Fore.WHITE}
|                                    {Fore.GREEN}    |{Fore.WHITE}
|                                    {Fore.GREEN} ___|{Fore.WHITE}
|                                    {Fore.GREEN}|   |{Fore.WHITE}
|  _____                             {Fore.GREEN}|   |{Fore.WHITE}
| |     |           N                {Fore.GREEN}|   |{Fore.WHITE}
| |     |         W + {Fore.GREEN}E{Fore.WHITE}              {Fore.GREEN}|   |{Fore.WHITE}
| |     |           S                {Fore.GREEN}|   |{Fore.WHITE}
| |_____|                            {Fore.GREEN}|   |{Fore.WHITE}
|                                    {Fore.GREEN}|   |{Fore.WHITE}
|                                    {Fore.GREEN}|   |{Fore.WHITE}
|               __________           {Fore.GREEN}|   |{Fore.WHITE}
|              |          |          {Fore.GREEN}|   |{Fore.WHITE}
|           |  |          |  |       {Fore.GREEN}|___|{Fore.WHITE}
|           |  |          |  |       {Fore.GREEN}    |{Fore.WHITE}
|______________|__________|__________{Fore.GREEN}____|{Fore.WHITE}
"""

ROOM_DESIGN_SOUTH = f"""
 ________________________________________
|             |___________|              |
|                                        |
|                                     ___|
|                                    |   |
|  _____                             |   |
| |     |           N                |   |
| |     |         W + E              |   |
| |     |           {Fore.RED}S{Fore.WHITE}                |   |
| |_____|                            |   |
|                                    |   |
|                                    |   |
{Fore.RED}|               __________           |   |
|              |          |          |   |
|           |  |          |  |       |___|
|           |  |          |  |           |
|______________|__________|______________| {Fore.WHITE}
"""

ROOM_DESIGN_WEST = f"""
{Fore.YELLOW} __________{Fore.WHITE}______________________________
{Fore.YELLOW}|         {Fore.WHITE}    |___________|              |
{Fore.YELLOW}|         {Fore.WHITE}                               |
{Fore.YELLOW}|         {Fore.WHITE}                            ___|
{Fore.YELLOW}|         {Fore.WHITE}                           |   |
{Fore.YELLOW}|  _____  {Fore.WHITE}                           |   |
{Fore.YELLOW}| |     | {Fore.WHITE}          N                |   |
{Fore.YELLOW}| |     | {Fore.WHITE}        {Fore.YELLOW}W{Fore.WHITE} + E              |   |
{Fore.YELLOW}| |     | {Fore.WHITE}          S                |   |
{Fore.YELLOW}| |_____| {Fore.WHITE}                           |   |
{Fore.YELLOW}|         {Fore.WHITE}                           |   |
{Fore.YELLOW}|         {Fore.WHITE}                           |   |
{Fore.YELLOW}|         {Fore.WHITE}      __________           |   |
{Fore.YELLOW}|         {Fore.WHITE}     |          |          |   |
{Fore.YELLOW}|         {Fore.WHITE}  |  |          |  |       |___|
{Fore.YELLOW}|         {Fore.WHITE}  |  |          |  |           |
{Fore.YELLOW}|_________{Fore.WHITE}_____|__________|______________|
"""

MAIN_TEXT = """
Welcome to the Escape Room. This game will test your problem solving 
skills and creativity. You will be dropped in a room and you will have to 
think of different commands to get yourself out of the room.
"""

INFORMATION_TEXT = """
  _____ _   _ ______ ____  _____  __  __       _______ _____ ____  _   _ 
 |_   _| \ | |  ____/ __ \|  __ \|  \/  |   /\|__   __|_   _/ __ \| \ | |
   | | |  \| | |__ | |  | | |__) | \  / |  /  \  | |    | || |  | |  \| |
   | | | . ` |  __|| |  | |  _  /| |\/| | / /\ \ | |    | || |  | | . ` |
  _| |_| |\  | |   | |__| | | \ \| |  | |/ ____ \| |   _| || |__| | |\  |
 |_____|_| \_|_|    \____/|_|  \_\_|  |_/_/    \_\_|  |_____\____/|_| \_|
___________________________________________________________________________

Want to learn how to play the Escape Room game? Well it is very simple and easy. 
Your job is to escape the room and search for hidden clues and messages with commands.
You will be given a scenario and you can give a command to further the story. The command 
can be anything related to the scenario. For Example: The scenario is as follow...\n
You find yourself in a car... What do you do?\n

You can answer anything down the line like:
Answer: Start the car\n
Answer: Look around the car\n
and so on.\n

Depending on your answer, the story will progress accordingly.
"""

STORY_START = """
You find yourself in a small room. You feel foggy and you dont know where you are or how you got here. 
You get the feeling that you need to get out of this room...\n
What do you do?
"""

STORY_NORTH_INSPECT = f"""
You see that there is a \033[5;35mPurple\033[0;0m combination padlock on the door, 
it seems like it needs a \033[5;35m4 digit\033[0;0m code to unlock. Do you want to unlock the door? (Y/N)
"""

STORY_EAST_INSPECT = f"""
You see a bookshelf filled with different colour books, the person who this room belongs 
to must really love reading! The different colour books are mesmerising to look at. As you are inspecting 
the bookshelf, you notice that there are a lot of different colour books but only \033[5;35m4 Purple\033[0;0m and \033[5;31m4 Red\033[0;0m books.\n
What do you do?
"""

INSPECT_BOOK_PURPLE = f"""
After inspecting the purple books, you notice that each of the book have a number and alphabet each. 
The first book you picked up has a letter {Fore.LIGHTCYAN_EX}K{Fore.WHITE} and a number {Fore.LIGHTCYAN_EX}0{Fore.WHITE} on it, 
the second book has the letter {Fore.LIGHTGREEN_EX}Y{Fore.WHITE} and number {Fore.LIGHTGREEN_EX}2{Fore.WHITE} on it. 
The third book has the letter {Fore.LIGHTMAGENTA_EX}E{Fore.WHITE} and a number {Fore.LIGHTMAGENTA_EX}3{Fore.WHITE} on it. 
The forth Book has a letter {Fore.LIGHTYELLOW_EX}Q{Fore.WHITE} and … no number? It seems like a sticker of a ostrobogulous duck was on the area where the number should be. 
Something sharp will work to scratch off this weird sticker.\n
What do you do?
"""

SUICIDE_TEXT = """
              _ _  _____ _______ ____  _____  _ _ 
            | | |/ ____|__   __/ __ \|  __ \| | |
            | | | (___    | | | |  | | |__) | | |
            | | |\___ \   | | | |  | |  ___/| | |
            |_|_|____) |  | | | |__| | |    |_|_|
            (_|_)_____/   |_|  \____/|_|    (_|_)
            _______________________________________
   _____   ____  _   _ _ _______   _____   ____    _____ _______ 
 |  __ \ / __ \| \ | ( )__   __| |  __ \ / __ \  |_   _|__   __|
 | |  | | |  | |  \| |/   | |    | |  | | |  | |   | |    | |   
 | |  | | |  | | . ` |    | |    | |  | | |  | |   | |    | |   
 | |__| | |__| | |\  |    | |    | |__| | |__| |  _| |_   | |   
 |_____/ \____/|_| \_|    |_|    |_____/ \____/  |_____|  |_|   
_________________________________________________________________
"""

INSPECT_BOOK_RED = f"""
You take the first red book you see, the outside of the book doesnt 
seem like it has anything special to it, do you open the book? (Y/N)
"""

INSPECT_CHAIRS = f"""
You approach the table and chairs, as you get closer, you notice that there is nothing to notice with the table and chairs. 
Nothing special to see here.\n
"""

SIT_CHAIRS = f"""
You walk closer to the table, pull back the chair and sit on the chair… As you are sitting, you start to think about your situation. 
You wonder how on earth you got in this mysterious room and why you have no memory of how you got here. You fall into deep thought, 
the more you think the faster time feels, but there is no way of knowing how much time has passed since there is no way of 
keeping track of time in this room. 
3 hours passed by.\n
"""

STAND_CHAIR = f"""
You walk closer with determination, climb on and Yell “HAH! King Of the Hill!!”… As you say it you 
remember that you are the only one in the room. Personally, at this point Im worried about your insanity. 
Please Get off the table.\n
"""

DESK_INPSECT = """
You approach the desk, as you get closer, you first notice the knife on the desk. Afterwards you see that the desk also have 2 drawers. 
What do you do?\n
"""

LEFT_DRAWER = """
The drawer is very difficult to open, but you pull harder. You used all your strength to open this one drawer... but it is shut tightly. 
I dont think it should open.\n
"""


OPEN_RED_BOOK = f"""
You open the book… You start reading the first line, the book was so interesting, that you spend almost 
2 hours just standing there and reading this book… Fascinating! But… your legs are kinda sore. 
You have a feeling that the other red books will have the same results.
"""

ESCAPED_MSG = """
 __     ______  _    _ _ _____  ______   ______ _____  ______ ______ _ _ 
 \ \   / / __ \| |  | ( )  __ \|  ____| |  ____|  __ \|  ____|  ____| | |
  \ \_/ / |  | | |  | |/| |__) | |__    | |__  | |__) | |__  | |__  | | |
   \   /| |  | | |  | | |  _  /|  __|   |  __| |  _  /|  __| |  __| | | |
    | | | |__| | |__| | | | \ \| |____  | |    | | \ \| |____| |____|_|_|
    |_|  \____/ \____/  |_|  \_\______| |_|    |_|  \_\______|______(_|_)
__________________________________________________________________________

Congratulations! You have managed to escaped the room. 
"""

GOODBYE = """
   _____  ____   ____  _____  ______     ________ _ _ 
  / ____|/ __ \ / __ \|  __ \|  _ \ \   / /  ____| | |
 | |  __| |  | | |  | | |  | | |_) \ \_/ /| |__  | | |
 | | |_ | |  | | |  | | |  | |  _ < \   / |  __| | | |
 | |__| | |__| | |__| | |__| | |_) | | |  | |____|_|_|
  \_____|\____/ \____/|_____/|____/  |_|  |______(_|_)
________________________________________________________
"""

TIPS_1 = """
Life Tip:
The greatest glory in living lies not in never falling, but in rising every time we fall.

- Nelson Mandela
"""

TIPS_2 = """
Life Tip:
The way to get started is to quit talking and begin doing. 

- Walt Disney
"""

TIPS_3 = """
Life Tip:
Your time is limited, so don't waste it living someone else's life. 
Don't be trapped by dogma, which is living with the results of other people's thinking. 

- Steve Jobs
"""

TIPS_4 = """
Life Tip:
If life were predictable it would cease to be life, and be without flavor. 

- Eleanor Roosevelt
"""

TIPS_5 = """
Life Tip:
If you look at what you have in life, you'll always have more. 
If you look at what you don't have in life, you'll never have enough. 

- Oprah Winfrey
"""

TIPS_6 = """
Life Tip:
If you set your goals ridiculously high and it's a failure, 
you will fail above everyone else's success. 

- James Cameron

"""

TIPS_7 = """
Life Tip:
Life is what happens when you're busy making other plans. 

- John Lennon
"""

TIPS_8 = """
Life Tip:
Spread love everywhere you go. Let no one ever come to you without leaving happier. 

- Mother Teresa
"""

TIPS_9 = """
Life Tip:
Always remember that you are absolutely unique. Just like everyone else. 

- Margaret Mead
"""

TIPS_10 = """
Life Tip:
Don't judge each day by the harvest you reap but by the seeds that you plant. 

- Robert Louis Stevenson
"""