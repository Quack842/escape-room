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
You will be given a scenario and you can give a command to further the story. The command 
can be anything related to the scenario. For Example: The scenario is as follow...\n
You find yourself in a car... What do you do?\n

You can answer anything down the line like:
Answer: Start the car\n
Answer: Look around\n
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

STORY_NORTH_APPROACH = f"""
As you get closer to the door, you notice a \033[5;35mPurple\033[0;0m combination padlock on the door, 
it seems like you would need a \033[5;35m4 digit\033[0;0m code to unlock. Do you want to unlock the door? (Y/N)
"""

STORY_NORTH_OPEN = f"""
As you reached out to the door handle to open the door, you notice a \033[5;35mPurple\033[0;0m combination padlock. 
You first have to enter a \033[5;35m4 digit\033[0;0m code. Do you want to unlock the door? (Y/N)

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