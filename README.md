# Linux Learning Game

## Overview

The **Linux Learning Game** is an interactive, CLI-based tool designed to help users learn and practice Linux commands in a gamified way. The game offers challenges across multiple levels (Beginner, Intermediate, and Advanced) that test users' knowledge of essential Linux commands, system administration, file management, networking, security, and more.

This project is designed for users ranging from beginners to advanced Linux users, helping them to strengthen their command-line skills through a series of hands-on challenges.

---

## Features

- **Multiple Difficulty Levels**: Challenges are categorized into three levels: Beginner, Intermediate, and Advanced.
- **Real-World Use Cases**: Each challenge includes practical, real-world scenarios that help users understand the context and importance of each command.
- **Gamified Experience**: Users can complete challenges, earn points, and improve their Linux skills in an engaging, game-like environment.
- **CLI Interface**: Simple, colorful CLI interface that makes learning interactive and fun.

---

## Project Structure

The project is organized into the following directories and files:

```
linux_learning_game/
├── challenges/               # Directory containing challenges for each level (Beginner, Intermediate, Advanced)
│   ├── beginner.json
│   ├── intermediate.json
│   └── advanced.json
├── cli.py                    # Main CLI script that runs the game
├── engine.py                 # Core game logic (handling challenges, scoring, etc.)
├── levels.py                 # Manages challenge levels and the loading of challenges
├── scoring.py                # Handles user score management and leaderboard
├── utils.py                  # Utility functions for common tasks (e.g., clearing the screen, displaying instructions)
├── README.md                 # Project documentation
├── requirements.txt          # List of project dependencies
```

### **Key Files:**

- **`cli.py`**: The main script that provides the user interface for interacting with the game. It displays the menu, loads challenges, and handles user input.
- **`engine.py`**: Contains the logic for managing the gameplay, including running challenges, validating answers, and updating scores.
- **`levels.py`**: Defines the structure of the challenges for each difficulty level (Beginner, Intermediate, Advanced).
- **`scoring.py`**: Manages the score system and leaderboard.
- **`utils.py`**: Provides utility functions for clearing the terminal, displaying instructions, and other common tasks.
- **`challenges/`**: Contains JSON files for each difficulty level. Each file includes a set of challenges with descriptions, solutions, hints, and explanations.

---

## Installation

Follow these steps to set up the **Linux Learning Game** on your local machine:

### **1. Clone the Repository**

Clone the repository to your local machine using Git:

```bash
git clone https://github.com/SarangVehale/linux-learning-game.git
cd linux-learning-game
```

### **2. Install Dependencies**

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

This will install the necessary libraries, including `colorama` for color output in the terminal.

### **3. Run the Game**

To start the game, simply run the `cli.py` file:

```bash
python cli.py       #For windows
python3 cli.py      #For mac or linux
```

The game will start, and you'll be presented with the main menu where you can select a difficulty level and start completing challenges.

---

## How It Works

### **Challenge Structure**

Each challenge includes the following components:
- **Description**: A brief overview of what the user needs to do.
- **Solution**: The correct Linux command(s) to complete the challenge.
- **Hints**: Optional hints to assist the user if they get stuck.
- **Explanation**: A detailed explanation of the command and its components.
- **Learning Points**: Key takeaways from the challenge to help users understand the command and its usage.
- **Real-World Application**: Practical examples of how the command is used in real-world scenarios.

### **Challenge Levels**

- **Beginner Level**: Introduces fundamental Linux commands related to file management, navigation, and basic system tasks.
- **Intermediate Level**: Focuses on more advanced commands related to system monitoring, network management, and process handling.
- **Advanced Level**: Covers topics like user and group management, system security, automation, and troubleshooting.

### **Scoring System**

As you complete challenges, you earn points:
- **Correct Answer**: 10 points
- **Hints Used**: Deduct 5 points per hint used

You can track your progress and view the leaderboard to compare your score with others.

---

## Contributing

Contributions are welcome! If you have any suggestions or want to add more challenges, feel free to fork the repository and submit a pull request.

### How to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Add your changes and commit them (`git commit -am 'Add new challenge'`).
4. Push to the branch (`git push origin feature-name`).
5. Submit a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Colorama** for adding color to the terminal interface.
- **Linux Foundation** for providing comprehensive resources on Linux commands.
- **The open-source community** for contributing to various Linux utilities and tools.
---

