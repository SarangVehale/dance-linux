# Tests for Linux Learning Game

This directory contains unit tests for the **Linux Learning Game** project. The tests are designed to verify the functionality of various modules and features of the game, including challenge loading, scoring, command execution, user input handling, and more. These tests ensure that the game runs correctly and meets the expected functionality.

## Test Structure

The tests are organized into the following files:

- **`test_game.py`**: Contains unit tests for the core game logic, including:
  - Initialization of game components (e.g., game engine, levels, scoring).
  - Challenge loading and handling.
  - Scoring updates, including the effect of hints.
  - Menu display, user input handling, and command execution.
  - End-of-game behavior and leaderboard functionality.
  
## Running the Tests

To run the tests, follow these steps:

### 1. Install Dependencies

Before running the tests, ensure that all dependencies are installed. If you haven't done so already, run the following command to install the required libraries:

```bash
pip install -r requirements.txt
```

This will install necessary dependencies, such as `unittest`.

### 2. Run the Tests

You can run the tests using the `unittest` module in Python. Simply execute the following command from the root directory of the project:

```bash
python -m unittest discover tests/
```

This command will search for all test files in the `tests/` directory and run them automatically. The output will show the results of each test case.

Alternatively, if you want to run the specific test file (e.g., `test_game.py`), use this command:

```bash
python -m unittest tests.test_game
```

### 3. Test Output

The test results will be displayed in the terminal. If all tests pass, you will see a message indicating success. If any tests fail, you will get a detailed error message to help you troubleshoot the issues.

Example output (if all tests pass):

```bash
----------------------------------------------------------------------
Ran 12 tests in 0.001s

OK
```

If any tests fail, the output will indicate which tests failed and provide details about the failure.

### 4. Code Coverage (Optional)

To ensure that all parts of the code are being tested, you can run the tests with **coverage** to measure code coverage. Install the `coverage` package by running:

```bash
pip install coverage
```

Then, run the tests with coverage enabled:

```bash
coverage run -m unittest discover tests/
coverage report
```

This will show a report indicating which lines of code are covered by the tests and which lines are not.

## Test Details

### Test Files

- **`test_game.py`**: This file contains comprehensive tests for the main features of the game, ensuring that the game logic works as expected, including:
  - The initialization of the game engine, levels, and scoring.
  - Correct challenge loading and scoring updates.
  - Verification that user input is handled correctly.
  - Ensuring that commands are executed and game results are shown.

### Mocking and Patching

Some of the tests use **mocking** and **patching** with `unittest.mock` to simulate user input, command execution, and other behaviors. This is useful for isolating specific functionality and avoiding reliance on external systems or real user input.

For example, in the `test_display_menu` test, the output is captured using `patch` to verify that the main menu is displayed correctly without requiring manual interaction.

### Code Coverage

To ensure all aspects of the game are tested, the tests aim to cover:
- Challenge loading and content validation.
- Score calculation (including hints and challenge completion).
- Correct display of menus, help text, and leaderboards.
- Proper interaction with system commands (like `ls`, `cat`, etc.) using mocked subprocess calls.

## Contributing to Tests

If you find bugs or issues with the game, you can contribute to improving the test suite by following these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b add-new-test`).
3. Add your new test cases to the appropriate test file.
4. Run all tests to ensure that the new tests do not break existing functionality.
5. Submit a pull request.

Make sure to include detailed explanations in the test cases for new features or bug fixes.

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Conclusion

The tests in this folder ensure that the **Linux Learning Game** functions as expected and that each feature works correctly. By running these tests regularly, we can ensure that the game remains reliable and bug-free as new features are added or changes are made.

Feel free to run the tests and contribute to improving the game's functionality!

---

