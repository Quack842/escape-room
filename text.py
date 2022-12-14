"""
Start of the Project and File
"""
import colorama
from colorama import Fore
# from run import USERNAME
colorama.init()

TITLE = f"""
_________________________________________________________________

{Fore.BLUE}███████╗███████╗ ██████╗ █████╗ ██████╗ ███████╗             
██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝             
█████╗  ███████╗██║     ███████║██████╔╝█████╗{Fore.LIGHTBLACK_EX}              
██╔══╝  ╚════██║██║     ██╔══██║██╔═══╝ ██╔══╝               
███████╗███████║╚██████╗██║  ██║██║     ███████╗             
╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚══════╝ {Fore.LIGHTBLUE_EX}            
                        ██████╗  ██████╗  ██████╗ ███╗   ███╗
                        ██╔══██╗██╔═══██╗██╔═══██╗████╗ ████║
                        ██████╔╝██║   ██║██║   ██║██╔████╔██║{Fore.LIGHTBLACK_EX}
                        ██╔══██╗██║   ██║██║   ██║██║╚██╔╝██║
                        ██║  ██║╚██████╔╝╚██████╔╝██║ ╚═╝ ██║
                        ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝{Fore.WHITE}
_______________________________________________________________                                                                                     
"""

# Room Designs

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
skills and creativity. Use your imagination to escape!
"""

START_TEXT = f"""
To start the game, type {Fore.BLUE}start{Fore.WHITE}. If you want to know more 
about the game and how to play this game type {Fore.BLUE}Info/Information{Fore.WHITE}. 
Whenever you want to exit the app, just type {Fore.BLUE}kill code{Fore.WHITE}.
"""

INVALID_COMMAND = f"""
{Fore.RED}Invalid Command.{Fore.WHITE} Please make sure of spelling and enter a valid command...
"""

INFORMATION_TEXT = f"""
  _____ _   _ ______ ____  _____  __  __       _______ _____ ____  _   _ 
 |_   _| \ | |  ____/ __ \|  __ \|  \/  |   /\|__   __|_   _/ __ \| \ | |
   | | |  \| | |__ | |  | | |__) | \  / |  /  \  | |    | || |  | |  \| |
   | | | . ` |  __|| |  | |  _  /| |\/| | / /\ \ | |    | || |  | | . ` |
  _| |_| |\  | |   | |__| | | \ \| |  | |/ ____ \| |   _| || |__| | |\  |
 |_____|_| \_|_|    \____/|_|  \_\_|  |_/_/    \_\_|  |_____\____/|_| \_|
___________________________________________________________________________

Want to learn how to play the Escape Room game? Well it is very simple and easy. 
Your job is to escape the room and search for hidden clues and messages with 
commands. You will be given a scenario and you can give a command to further the
story. The command can be anything related to the scenario. For Example: The 
scenario is as follow... You find yourself in a car... What do you do?

You can answer anything down the line like:
Answer: Start the car
Answer: Look around the car
and so on.

Depending on your answer, the story will progress accordingly.
You can change the direction you're facing by indicating which direction you 
want to face. There is also tips and hints available, just type a sentence with 
the word {Fore.BLUE}"hint"{Fore.WHITE} or {Fore.BLUE}"tip"{Fore.WHITE} in it.
"""

# Start of the story

STORY_START = """
You find yourself in a small room. You feel foggy and you don't know where you 
are or how you got here. You get the feeling that you need to get out of this 
room...\n
What do you do """

WHERE_LOOK = f"""
Where do you look?
Forward{Fore.BLUE}(NORTH){Fore.WHITE}, To Your Right{Fore.GREEN}(East){Fore.WHITE}, Behind You{Fore.RED}(South){Fore.WHITE} or to Your Left{Fore.YELLOW}(West){Fore.WHITE}
"""

# Random commands text

LOOK_UP = """
You look up... there is a single light bulb flickering above you... 
Just don't go into the light.\n
"""

LOOK_DOWN = """
You look down... you're looking at your feet... I wonder if you'll use them.\n
"""

KICK_LOOK = """
Why would you kick?... What would you kick? What will this achieve?...
Do anything else
"""

# Text for killing the code

KILL_CODE = f"""
Are you positive you want to quit the app?
Type {Fore.BLUE}Y{Fore.WHITE} if you want to quit the app or type {Fore.BLUE}N{Fore.WHITE} if 
you want to stay and try again.\n
"""

# When the user inpsect the north

STORY_NORTH_INSPECT = f"""
You see that there is a \033[5;35mPurple\033[0;0m combination padlock on the 
door, it seems like it needs a \033[5;35m4 digit\033[0;0m code to unlock. Do you 
want to unlock the door?(Y/N)
"""

FACE_NORTH_START = f"""
{Fore.BLUE}North:{Fore.WHITE} You see a door… What do you do """

# When the user inspect the east side

STORY_EAST_INSPECT = f"""
You see a bookshelf filled with different colour books, the person who this room 
belongs to must really love reading! The different colour books are mesmerising 
to look at. As you are inspecting the bookshelf, you notice that there are a lot 
of different colour books but only \033[5;35m4 Purple\033[0;0m and \033[5;31m4 Red\033[0;0m books.\n
What do you do?
"""

# When the user inspect the books

INSPECT_BOOK_PURPLE = f"""
After inspecting the purple books, you notice that each of the book have a 
number and alphabet each. The {Fore.LIGHTCYAN_EX}first{Fore.WHITE} book you picked up has a letter {Fore.LIGHTCYAN_EX}K{Fore.WHITE} and a 
number {Fore.LIGHTCYAN_EX}0{Fore.WHITE} on it, the {Fore.LIGHTGREEN_EX}second{Fore.WHITE} book has the letter {Fore.LIGHTGREEN_EX}Y{Fore.WHITE} and 
number {Fore.LIGHTGREEN_EX}2{Fore.WHITE} on it. The {Fore.LIGHTMAGENTA_EX}third{Fore.WHITE} book has the letter {Fore.LIGHTMAGENTA_EX}E{Fore.WHITE} and a number {Fore.LIGHTMAGENTA_EX}3{Fore.WHITE} on it. 
The {Fore.LIGHTYELLOW_EX}forth{Fore.WHITE} Book has a letter {Fore.LIGHTYELLOW_EX}Q{Fore.WHITE} and … no number? It seems like a sticker of a 
ostrobogulous duck was on the area where the number should be. Something 
sharp will work to scratch off this weird sticker.\n
What do you do """

INSPECT_BOOK_RED = f"""
You take the first red book you see, the outside of the book doesn't 
seem like it has anything special to it, do you open the book? (Y/N)
"""

# When the user commands anything suicidal, you might wonder who would do this...
# I asked my brother to test my code and the first thing he typed was
# die...

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

# The different scenarios for the south direction

INSPECT_CHAIRS = f"""
You approach the table and chairs, as you get closer, you notice that there is 
nothing to notice with the table and chairs. 
Nothing special to see here.\n
"""

SIT_CHAIRS = f"""
You walk closer to the table, pull back the chair and sit on the chair… As you 
are sitting, you start to think about your situation. You wonder how on earth you 
got in this mysterious room and why you have no memory of how you got here. You 
fall into deep thought, the more you think the faster time feels, but there is 
no way of knowing how much time has passed since there is no way of keeping 
track of time in this room. 3 hours passed by...\n
"""

STAND_CHAIR = f"""
You walk closer with determination, climb on and Yell “HAH! King Of the Hill!!”… 
As you say it you remember that you are the only one in the room. Personally, 
at this point Im worried about your insanity. 
Please Get off of my table.\n
"""

DESK_INPSECT = """
You approach the desk, as you get closer, you notice the knife on the desk.
This might come in handy later. Afterwards you see that the desk also have 2 drawers. 
What do you do """

# When the user wants to open one of the drawers

LEFT_DRAWER = """
The drawer is very difficult to open, but you pull harder. You used all your strength 
to open this one drawer... but it is shut tightly. 
I don't think it should open.\n
"""

RIGHT_DRAWER = """
You try to pull on the right drawer, it is difficult to open, it might be stuck.
Why would the story teller even mention the drawers if they don't open? What
mind games are being played here?\n
"""

#When the user inspect the red books

OPEN_RED_BOOK = f"""
You open the book… You start reading the first line, the book was so interesting, that 
you spend almost 2 hours just standing there and reading this book… Fascinating! 
But… your legs are kinda sore. You have a feeling that the other red books will have 
the same results.\n
"""

# When the user search around

SEARCH_COMMAND = """
After looking around, you notice something sharp to the west side.
"""

#When the user escapes the room

ESCAPED_MSG = f"""
{Fore.BLUE} __     ______  _    _ _ _____  ______   ______ _____  ______ ______ _ _ 
 \ \   / / __ \| |  | ( )  __ \|  ____| |  ____|  __ \|  ____|  ____| | |
  \ \_/ / |  | | |  | |/| |__) | |__    | |__  | |__) | |__  | |__  | | |{Fore.GREEN}
   \   /| |  | | |  | | |  _  /|  __|   |  __| |  _  /|  __| |  __| | | |{Fore.RED}
    | | | |__| | |__| | | | \ \| |____  | |    | | \ \| |____| |____|_|_|{Fore.YELLOW}
    |_|  \____/ \____/  |_|  \_\______| |_|    |_|  \_\______|______(_|_){Fore.WHITE}
__________________________________________________________________________

Congratulations! You have managed to escape the room.

Walking out of the escape room, you get the since that
you have overcome a huge mountain...
when in reality.. you just finished a game
where you could have gotten the unlock code
from the github source code.

Thank You for playing and I hope you have a wonderful day!! 
"""

# When the user quits the app

GOODBYE = """
   _____  ____   ____  _____  ______     ________ _ _ 
  / ____|/ __ \ / __ \|  __ \|  _ \ \   / /  ____| | |
 | |  __| |  | | |  | | |  | | |_) \ \_/ /| |__  | | |
 | | |_ | |  | | |  | | |  | |  _ < \   / |  __| | | |
 | |__| | |__| | |__| | |__| | |_) | | |  | |____|_|_|
  \_____|\____/ \____/|_____/|____/  |_|  |______(_|_)
________________________________________________________
"""

# When the user enters TIPS instead of hint, they will get life tips...

TIPS_1 = f"""
{Fore.BLUE}Life Tip:{Fore.WHITE}
The greatest glory in living lies not in never falling, but in rising every time we fall.

- Nelson Mandela
"""

TIPS_2 = f"""
{Fore.GREEN}Life Tip:{Fore.WHITE}
The way to get started is to quit talking and begin doing. 

- Walt Disney
"""

TIPS_3 = f"""
{Fore.YELLOW}Life Tip:{Fore.WHITE}
Your time is limited, so don't waste it living someone else's life. 
Don't be trapped by dogma, which is living with the results of other people's thinking. 

- Steve Jobs
"""

TIPS_4 = f"""
{Fore.MAGENTA}Life Tip:{Fore.WHITE}
If life were predictable it would cease to be life, and be without flavor. 

- Eleanor Roosevelt
"""

TIPS_5 = f"""
{Fore.LIGHTBLUE_EX}Life Tip:{Fore.WHITE}
If you look at what you have in life, you'll always have more. 
If you look at what you don't have in life, you'll never have enough. 

- Oprah Winfrey
"""

TIPS_6 = f"""
{Fore.LIGHTGREEN_EX}Life Tip:{Fore.WHITE}
If you set your goals ridiculously high and it's a failure, 
you will fail above everyone else's success. 

- James Cameron

"""

TIPS_7 = f"""
{Fore.LIGHTYELLOW_EX}Life Tip:{Fore.WHITE}
Life is what happens when you're busy making other plans. 

- John Lennon
"""

TIPS_8 = f"""
{Fore.LIGHTMAGENTA_EX}Life Tip:{Fore.WHITE}
Spread love everywhere you go. Let no one ever come to you without leaving 
happier. 

- Mother Teresa
"""

TIPS_9 = f"""
{Fore.CYAN}Life Tip:{Fore.WHITE}
Always remember that you are absolutely unique. Just like everyone else. 

- Margaret Mead
"""

TIPS_10 = f"""
{Fore.LIGHTCYAN_EX}Life Tip:{Fore.WHITE}
Don't judge each day by the harvest you reap but by the seeds that you plant. 

- Robert Louis Stevenson\n
"""
# HINT FOR THE USER WHEN THEY NEE HELP
HINT_1 = f"""
{Fore.BLUE}Hint - 1:{Fore.WHITE}
When you are stuck, just type "back", this will take you back to where you can face any direction.
"""

HINT_2 = f"""
{Fore.GREEN}Hint - 2:{Fore.WHITE}
Search around the room, if you are stuck, try using commands that has one of the following words in it:
- look
- inspect
- approach
"""

HINT_3 = f"""
{Fore.YELLOW}Hint - 3:{Fore.WHITE}
If you are stuck and the other hints doesn't work, you can always kill the game by typing "kill code".
"""

HINT_4 = f"""
{Fore.MAGENTA}Hint - 4:{Fore.WHITE}
There might be something at the bookshelf, that is to the east of the room.
"""

HINT_5 = f"""
{Fore.LIGHTCYAN_EX}Hint - 5:{Fore.WHITE}
It helps to specify which direction you want to look at, sometimes.
"""

HINT_6 = f"""
{Fore.LIGHTGREEN_EX}Hint - 6:{Fore.WHITE}
There is no limit to the lock combination guesses, so you could always just guess the code.
"""

HINT_7 = f"""
{Fore.LIGHTYELLOW_EX}Hint - 7:{Fore.WHITE}
You can always get the code to the combination lock in the source code... but 
that is cheating
"""

HINT_8 = f"""
{Fore.LIGHTMAGENTA_EX}Hint - 8:{Fore.WHITE}
You can always change the direction you are facing by typing "turn to the left" or "turn to the right".
"""

HINT_9 = f"""
{Fore.CYAN}Hint - 9:{Fore.WHITE}
The first letter is the first number.
"""

# Error Messages
USERNAME_SHORT_ERROR = f"""
{Fore.RED}The Length of the username is too short, please try again{Fore.WHITE}
"""

USERNAME_LONG_ERROR = f"""
{Fore.RED}The username is too long, try a shorter username.{Fore.WHITE}
"""

USERNAME_NUMBERS = f"""
{Fore.RED}The username cannot contain any numbers.{Fore.WHITE}
"""

USERNAME_SYMBOLS = f"""
{Fore.RED}Your name cannot contain any symbols, please try again.{Fore.WHITE}
"""