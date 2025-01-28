import json
import subprocess
from time import sleep
from colorama import Fore, Style
from utils import clear_screen, show_message_with_delay
from scoring import update_score


def load_challenges(level):
    """
    Load challenges from the JSON file for the given level.

    Args:
        level (str): The difficulty level (e.g., beginner, intermediate, advanced).

    Returns:
        list: A list of challenges loaded from the JSON file.
    """
    try:
        with open(f"challenges/{level}.json", "r") as file:
            return json.load(file)["challenges"]
    except FileNotFoundError:
        print(Fore.RED + f"Error: Challenges for level '{level}' not found!")
        return []
    except json.JSONDecodeError:
        print(Fore.RED + f"Error: Invalid JSON format in '{level}.json'.")
        return []


def validate_command(user_input, solution):
    """
    Validate the user input command by comparing it to the solution.

    Args:
        user_input (str): The user's command.
        solution (str): The correct solution command.

    Returns:
        bool: True if the command output matches the solution, False otherwise.
    """
    try:
        # Split the solution into required command and keywords for validation
        required_command, *keywords = solution.split(" || ")

        # Execute user's command
        result = subprocess.check_output(user_input, shell=True, text=True).strip()

        # Check if the user's command matches the required command
        if user_input.strip() == required_command.strip():
            return True

        # If not an exact match, check for the presence of required keywords in the output
        for keyword in keywords:
            if keyword.strip() not in result:
                return False

        return True
    except subprocess.CalledProcessError:
        return False


def start_game():
    """
    Main function to start the Linux Learning Game.
    """
    clear_screen()
    print(Fore.CYAN + "Select Difficulty Level:")
    print(Fore.YELLOW + "1. Beginner")
    print(Fore.MAGENTA + "2. Intermediate")
    print(Fore.RED + "3. Advanced")

    level_choice = input(Fore.WHITE + "\nEnter your choice: ").strip()
    levels = {"1": "beginner", "2": "intermediate", "3": "advanced"}
    level = levels.get(level_choice)

    if not level:
        print(Fore.RED + "Invalid level choice! Returning to main menu...")
        sleep(2)
        return 0  # Return 0 score when invalid choice is made

    # Prompt for user name at the start of the game
    user_name = input(Fore.YELLOW + "\nEnter your name: ").strip()

    # Load challenges
    challenges = load_challenges(level)
    if not challenges:
        sleep(2)
        return 0  # Return 0 score if no challenges found

    print(Fore.GREEN + f"\nStarting {level.capitalize()} Level... Good luck!")
    sleep(2)

    # Track score
    score = 0

    # Start challenges
    for index, challenge in enumerate(challenges, start=1):
        clear_screen()
        print(Fore.YELLOW + f"Challenge {index}:")
        print(Fore.CYAN + challenge["description"])

        # Hint mechanism
        hints_used = 0
        while True:
            user_input = input(Fore.WHITE + "\nEnter your command (or type 'hint'): ").strip()

            if user_input.lower() == "hint":
                if hints_used < len(challenge["hints"]):
                    print(Fore.MAGENTA + "Hint: " + challenge["hints"][hints_used])
                    hints_used += 1
                    score = max(0, score - 5)  # Deduct points for using hints, minimum score is 0
                else:
                    print(Fore.RED + "No more hints available!")

            elif user_input.lower() == "exit":
                print(Fore.RED + "\nExiting the challenge. Returning to main menu...")
                show_message_with_delay("", 2)
                return score  # Return score before exiting

            elif validate_command(user_input, challenge["solution"]):
                print(Fore.GREEN + "Correct! +10 points")
                score += 10

                # Show explanation and real-world application after correct answer
                if "explanation" in challenge:
                    print(Fore.CYAN + "\nExplanation: " + challenge["explanation"])
                if "real-world-application" in challenge:
                    print(Fore.YELLOW + "Real-world application: " + challenge["real-world-application"])

                # Wait for the user to acknowledge before proceeding
                input(Fore.WHITE + "\nPress Enter to continue to the next challenge...")
                break  # Exit the loop and proceed to the next challenge

            else:
                print(Fore.RED + "Incorrect! Try again.")

    # Update the leaderboard with the score and user name
    update_score(score, user_name)

    # Game completion message
    print(Fore.GREEN + f"\nCongratulations! You completed the {level.capitalize()} Level!")
    print(Fore.YELLOW + f"Your total score: {score}")
    show_message_with_delay("\nReturning to the main menu...", 3)
    return score  # Return final score at the end of the game

