import json
import os
from colorama import Fore
from time import sleep

# Path for leaderboard file
LEADERBOARD_FILE = "leaderboard.json"

def load_leaderboard():
    """Load the leaderboard data from the leaderboard.json file."""
    if not os.path.exists(LEADERBOARD_FILE):
        # If the leaderboard file doesn't exist, create an empty leaderboard file
        with open(LEADERBOARD_FILE, "w") as file:
            json.dump([], file, indent=4)
        print(Fore.YELLOW + "Leaderboard file not found, creating a new one.")
        return []  # Return empty list if file doesn't exist

    # If the file exists, try loading its content
    try:
        with open(LEADERBOARD_FILE, "r") as file:
            leaderboard = json.load(file)
            # If file is empty, return an empty list
            if not leaderboard:
                print(Fore.YELLOW + "Leaderboard file is empty.")
                return []
            return leaderboard
    except json.JSONDecodeError:
        # Handle the case where the file exists but is corrupted (non-JSON data)
        print(Fore.RED + "Error: Leaderboard file is corrupted. Resetting leaderboard.")
        # Reset the leaderboard to an empty list if the file is corrupted
        with open(LEADERBOARD_FILE, "w") as file:
            json.dump([], file, indent=4)
        return []

def save_leaderboard(leaderboard):
    """Save the leaderboard data to the leaderboard.json file."""
    try:
        with open(LEADERBOARD_FILE, "w") as file:
            json.dump(leaderboard, file, indent=4)
        print(Fore.GREEN + "Leaderboard saved successfully!")
    except Exception as e:
        print(Fore.RED + f"Error saving leaderboard: {e}")

def update_score(score, user_name):
    """Update the leaderboard with the latest score."""
    print(Fore.YELLOW + f"Updating leaderboard with {user_name}'s score: {score}...")

    leaderboard = load_leaderboard()  # Load existing leaderboard
    print(Fore.YELLOW + f"Current leaderboard before update: {leaderboard}")

    # Add the new score to the leaderboard
    leaderboard.append({"name": user_name, "score": score})

    # Sort the leaderboard by score in descending order
    leaderboard = sorted(leaderboard, key=lambda x: x["score"], reverse=True)

    # Keep only top 5 scores
    leaderboard = leaderboard[:5]

    # Save the updated leaderboard
    save_leaderboard(leaderboard)
    
    print(Fore.YELLOW + f"Leaderboard after update: {leaderboard}")

    print(Fore.GREEN + "\nScore updated successfully!")
    show_leaderboard(score)  # Show the leaderboard after updating

def show_leaderboard(current_score=None):
    """Display the leaderboard with the current score."""
    leaderboard = load_leaderboard()  # Load the leaderboard data

    if leaderboard:
        print(Fore.CYAN + "\nLeaderboard:")
        print(Fore.YELLOW + "--------------------------")
        for i, entry in enumerate(leaderboard, start=1):
            print(Fore.MAGENTA + f"{i}. {entry['name']} - {entry['score']} points")
        print(Fore.YELLOW + "--------------------------")
    else:
        print(Fore.RED + "\nLeaderboard is empty. Play the game to see results!")

    # Display current score at the bottom if passed
    if current_score is not None:
        print(Fore.GREEN + f"Current Score: {current_score}")

def show_message_with_delay(message, delay=2):
    """Display a message and wait for a specific delay."""
    print(Fore.YELLOW + message)
    sleep(delay)

