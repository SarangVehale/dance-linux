import os
import sys
from time import sleep
from colorama import Fore

def clear_screen():
    """Clear the terminal screen."""
    if os.name == "nt":  # For Windows
        os.system("cls")
    else:  # For macOS and Linux
        os.system("clear")

def show_message_with_delay(message, delay=2):
    """
    Display a message and wait for a specific delay.
    Args:
        message (str): The message to display.
        delay (int): The time to wait in seconds (default: 2 seconds).
    """
    print(Fore.YELLOW + message)
    sleep(delay)

def display_instructions():
    """Display game instructions."""
    clear_screen()
    instructions = f"""
{Fore.CYAN}Welcome to the Linux Learning Game!

{Fore.YELLOW}How to Play:
1. Choose a difficulty level: Beginner, Intermediate, or Advanced.
2. Complete each challenge by typing the correct Linux command.
3. You can type 'hint' to get help, but it will cost points.
4. Your goal is to earn as many points as possible by completing challenges quickly and accurately.

{Fore.MAGENTA}Scoring:
- +10 points for every correct answer.
- -5 points for every hint used.

{Fore.GREEN}Good luck and have fun!

Press Enter to return to the main menu.
"""
    print(instructions)
    input(Fore.WHITE + "\nPress Enter to continue...")

def exit_game():
    """Gracefully exit the game."""
    print(Fore.RED + "\nThank you for playing! Goodbye!")
    sys.exit(0)

