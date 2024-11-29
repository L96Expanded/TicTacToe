# Tic-Tac-Toe AI with Game History and Leaderboard

This is a Python-based implementation of the classic Tic-Tac-Toe game. It includes several features such as an AI opponent using a Greedy algorithm, a game history tracker, a player leaderboard, and functionalities for searching and displaying game statistics.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Code Structure](#code-structure)
- [Algorithms Used](#algorithms-used)
- [Time Complexities](#time-complexities)
- [Acknowledgments](#acknowledgments)

## Features

### Tic-Tac-Toe Gameplay:
- Two-player mode or play against AI.
- AI uses a Greedy algorithm for decision-making.

### Game History:
- Tracks details of all games, including players, winner, and whether the game ended in a draw.
- Sorts and displays games by date.

### Leaderboard:
- Tracks player statistics: wins, losses, and draws.
- Sorts leaderboard by wins.

### Search Functionalities:
- Search for a player in the leaderboard.
- Search for games involving a specific player.

## Requirements
- Python 3.7 or higher
- Standard Python libraries (datetime)
- flask library
  ```bash
   pip install flask

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/L96Expanded/TicTacToe.git
   cd tictactoe
If possible switch directly to the imported tictactoe folder, 
it still works either way, but saves time for refreshing

# How to Play

### Run the Game:
Execute `run.py` to start the program.

### Select Mode:
Choose between:
- Playing against another player.
- Playing against the AI.

### Input Moves:
Select on the on-screen gris a position.

### View Results:
After each game:
- Check the game history.
- View or search the leaderboard.

# Code Structure

### run.py
- starts and threads 'app.py' and 'main.py' as subprocesses and opens the website

## backend

### `main.py`:
- Entry point for the program.

### Game Logic:
- **`greedy_ai_move`**: Implements AI logic using a Greedy algorithm.
- **`check_winner`** and **`is_full`**: Evaluate game states.

### Game History and Leaderboard:
- **`display_game_history`**: Displays all games sorted by date.
- **`search_game_history`**: Search for games by player name.
- **`display_leaderboard`**: Displays the player leaderboard.
- **`search_leaderboard`**: Searches the leaderboard for a player.

### Utility Functions:
- Reusable helper functions are implemented in the helper module.
- Sorting algorithms in the `algos` module (e.g., quicksort).

## Frontend

### `app.py`:
- creates the python server used to host the website and stores the fetch 'GET' and 'POST' functions

### Website setup:
- **`index.html`**: Formats the website.
- **`style.css`**: stores the .css styles used in index.html.
- **`main.js`**: Stores the necessary javascript functions

# Algorithms Used

### Greedy Algorithm:
The AI evaluates moves based on a priority:
1. Take a winning move.
2. Block the opponent's winning move.
3. Take the center if available.
4. Occupy a corner or edge.

### Quicksort:
Used for sorting the leaderboard and game history.

# Time Complexities

### thread functions

| Function             | Best Case      | Average Case  | Worst Case    |
|----------------------|----------------|----------------|---------------|
| `run_script()`	              | O(1)           | O(1)           | O(1)          | 
| `__main__`	                 | O(1)           | O(1)           | O(1)          | 

## Backend functions 

### Game Functions

| Function             | Best Case      | Average Case  | Worst Case    |
|----------------------|----------------|----------------|---------------|
| `initialize_board`    | O(9)           | O(9)           | O(9)          |
| `display_board`       | O(1)           | O(1)           | O(1)          |
| `check_winner`        | O(1)           | O(3)           | O(9)          |
| `is_full`             | O(1)           | O(9)           | O(9)          |
| `play_round`          | O(1)           | O(9)           | O(9)          |

### General Algorithms

| Function             | Best Case      | Average Case  | Worst Case    |
|----------------------|----------------|----------------|---------------|
| `quicksort`           | O(n log n)     | O(n log n)     | O(n²)         |

### Leaderboard Functions

| Function             | Best Case      | Average Case  | Worst Case    |
|----------------------|----------------|----------------|---------------|
| `display_leaderboard` | O(n log n)     | O(n log n)     | O(n²)         |
| `search_leaderboard`  | O(1)           | O(n)           | O(n)          |
| `update_stats`        | O(1)           | O(1)           | O(1)          |

### Game History Functions

| Function             | Best Case      | Average Case  | Worst Case    |
|----------------------|----------------|----------------|---------------|
| `add_game_history`    | O(1)           | O(1)           | O(1)          |
| `display_game_history`| O(n) (display) | O(n log n)     | O(n²)         |
| `search_game_history` | O(n log n)     | O(n log n)     | O(n²)         |

### AI Functions

| Function             | Best Case      | Average Case  | Worst Case    |
|----------------------|----------------|----------------|---------------|
| `greedy_ai_move`      | O(1)           | O(9)           | O(9)          |
| `get_ai_move`         | O(1)           | O(9)           | O(9)          |

### Main Game Loop Functions

| Function             | Best Case      | Average Case  | Worst Case    |
|----------------------|----------------|----------------|---------------|
| `home_screen`         | O(1)           | O(1)           | O(1)          |
| `play_game`           | O(1)           | O(n)           | O(n)          |

## Frontend functions 

### Display website functions

| Function Name                | Best Case      | Average Case  | Worst Case    |
|------------------------------|----------------|----------------|---------------|
| `turn_change(event)`          | O(1)           | O(1)           | O(1)          |
| `make_grid(event)`            | O(9)           | O(9)           | O(9)          |
| `grid_hover_see(event)`       | O(1)           | O(1)           | O(1)          |
| `grid_hover_end(event)`       | O(1)           | O(1)           | O(1)          |
| `set_params(event)`           | O(1)           | O(1)           | O(1)          |

### Modify Display functions

| Function             | Best Case      | Average Case  | Worst Case    |
|----------------------|----------------|----------------|---------------|
| `hide(id)`                    | O(1)           | O(1)           | O(1)          |
| `show(id)`                    | O(1)           | O(1)           | O(1)          |
| `change(id1, id2)`            | O(1)           | O(1)           | O(1)          |

### Json functions

| Function             | Best Case      | Average Case  | Worst Case    |
|----------------------|----------------|----------------|---------------|
| `modifyJsonFile(key, value)`  | O(1)           | O(1)           | O(1)          |
| `getJsonFile()`               | O(1)           | O(1)           | O(1)          |

### Display popup functions

| Function             | Best Case      | Average Case  | Worst Case    |
|----------------------|----------------|----------------|---------------|
| `PVP()`                       | O(1)           | O(1)           | O(1)          |
| `PVAI()`                      | O(1)           | O(1)           | O(1)          |
| `Scoreboard()`                | O(1)           | O(n)           | O(n)          |
| `History()`                   | O(1)           | O(n)           | O(n)          |
| `show_end_popup()`            | O(1)           | O(1)           | O(1)          |
| `go_back_end()`               | O(1)           | O(1)           | O(1)          |
| `go_back_scoreboard()`        | O(1)           | O(1)           | O(1)          |
| `go_back_history()`           | O(1)           | O(1)           | O(1)          |

### Search button functions

| Function             | Best Case      | Average Case  | Worst Case    |
|----------------------|----------------|----------------|---------------|
| `search_history()`            | O(1)           | O(n)           | O(n)          |
| `search_scoreboard()`         | O(1)           | O(n)           | O(n)          |

### Set player functions

| Function             | Best Case      | Average Case  | Worst Case    |
|----------------------|----------------|----------------|---------------|
| `set_playerAI()`              | O(1)           | O(1)           | O(1)          |
| `set_player1()`               | O(1)           | O(1)           | O(1)          |
| `set_player2()`               | O(1)           | O(1)           | O(1)          |

### app functions

| Function             | Best Case      | Average Case  | Worst Case    |
|----------------------|----------------|----------------|---------------|
| `index()`                     | O(1)           | O(1)           | O(1)          | 
| `modify_json()`               | O(1)           | O(1)           | O(1)          | 
| `get_json_data()`             | O(1)           | O(1)           | O(1)          |


# Acknowledgments
This project was developed as part of a Computer Science algorithms course. It integrates general and AI algorithms, as well as various data structures in a Tic-Tac-Toe game.
