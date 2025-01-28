import sys
from time import sleep
from colorama import Fore, Style, init
from engine import start_game
from scoring import update_score, show_leaderboard
from utils import display_instructions, clear_screen

# Initialize colorama
init(autoreset=True)

def print_banner(score=0):
    """Display a colorful welcome banner and the current score."""
    banner = f"""
{Fore.CYAN}███████╗██╗     ██╗███╗   ██╗██╗   ██╗███████╗
{Fore.BLUE}██╔════╝██║     ██║████╗  ██║██║   ██║██╔════╝
{Fore.MAGENTA}█████╗  ██║     ██║██╔██╗ ██║██║   ██║█████╗
{Fore.YELLOW}██╔══╝  ██║     ██║██║╚██╗██║██║   ██║██╔══╝
{Fore.GREEN}███████╗███████╗██║██║ ╚████║╚██████╔╝███████╗
{Fore.RED}╚══════╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
    {Fore.WHITE}Welcome to the Linux Learning Game!
    {Fore.YELLOW}Current Score: {score} points
"""
    print(banner)
    sleep(1)

def main_menu(score):
    """Display the main menu with colorful options and current score."""
    print_banner(score)
    print(Fore.YELLOW + "Main Menu:")
    print(Fore.CYAN + "1. Start Game")
    print(Fore.GREEN + "2. View Leaderboard")
    print(Fore.MAGENTA + "3. Instructions")
    print(Fore.RED + "4. Exit")

def main():
    score = 0  # Track score globally
    while True:
        clear_screen()
        main_menu(score)
        choice = input(Fore.WHITE + "\nChoose an option: ").strip()

        if choice == "1":
            print(Fore.CYAN + "\nStarting the game... Good luck!")
            sleep(1)
            score = start_game()  # Start the game and get the score
        elif choice == "2":
            print(Fore.GREEN + "\nFetching the leaderboard...")
            sleep(1)
            show_leaderboard(score)  # Show leaderboard with the current score
            sleep(3)  # Pause for 3 seconds to let the user view the leaderboard before returning to the main menu
        elif choice == "3":
            display_instructions()
        elif choice == "4":
            print(Fore.RED + "\nThank you for playing! Goodbye!")
            sys.exit(0)
        else:
            print(Fore.RED + "\nInvalid option. Please try again.")
            sleep(1)

if __name__ == "__main__":
    main()

