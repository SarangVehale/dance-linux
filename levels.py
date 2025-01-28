import json
import os

def load_challenges(level):
    """
    Load challenges for the given difficulty level.
    Args:
        level (str): Difficulty level ('beginner', 'intermediate', 'advanced').

    Returns:
        list: A list of challenges for the given level.
    """
    challenge_file = f"challenges/{level}.json"
    
    # Check if the file exists
    if not os.path.exists(challenge_file):
        print(f"Error: Challenge file for '{level}' level does not exist.")
        return []

    try:
        with open(challenge_file, "r") as file:
            challenges = json.load(file)["challenges"]
        return challenges
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON in {level} challenge file.")
        return []

def display_challenges(challenges):
    """
    Display the challenges in a formatted way.
    Args:
        challenges (list): List of challenge dictionaries to display.
    """
    for i, challenge in enumerate(challenges, start=1):
        print(f"{i}. {challenge['description']}")
        print(f"   Hint(s): {', '.join(challenge.get('hints', ['No hints available']))}")

def get_challenge_solution(challenge_id, challenges):
    """
    Get the solution for a specific challenge by its ID.
    Args:
        challenge_id (int): The ID of the challenge.
        challenges (list): List of challenge dictionaries.
    
    Returns:
        str: The correct solution command for the challenge.
    """
    for challenge in challenges:
        if challenge["id"] == challenge_id:
            return challenge["solution"]
    return None

