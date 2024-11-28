from collections import deque
import ai
import leaderboard as lb
import gamehist as gh

# This section has functions which unify the algorithms and AI/leaderboard/game history functions to generate the game


def initialize_board():
    """
    Displays the current game board to the console.

    Time Complexity:
    - Best Case: O(9).
    - Average Case: O(9).
    - Worst Case: O(9).
    """

    return [[None for _ in range(3)] for _ in range(3)]


def display_board(board):
    """
    Displays the current game board to the console.

    Time Complexity:
    - Best Case: O(1) (Fixed 3x3 board display).
    - Average Case: O(1).
    - Worst Case: O(1).
    """

    print("\n".join([" | ".join([cell or " " for cell in row]) for row in board]))
    print("-" * 9)


def check_winner(board, player):
    """
    Checks if the given player has won the game.

    Time Complexity:
    - Best Case: O(1) (Winner is found in the first row, column, or diagonal checked).
    - Average Case: O(3) (Three iterations for rows, columns, or diagonals).
    - Worst Case: O(9) (Checks all rows, columns, and both diagonals).
    """
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_full(board):
    """
    Checks if the game board is completely filled with no empty spaces.

    Time Complexity:
    - Best Case: O(1) (Determined in the first iteration if an empty cell is found).
    - Average Case: O(9) (Iterates through the entire 3x3 grid once).
    - Worst Case: O(9) (Checks all cells when the board is completely filled).
    """
    return all(all(cell is not None for cell in row) for row in board)


def home_screen():
    """
    Generates a terminal-based UI for player interaction

    Time Complexity:
    - Best Case: O(1).
    - Average Case: O(1).
    - Worst Case: O(1).
    """

    print("\nWelcome to Tic-Tac-Toe!")
    print("1. Player vs Player")
    print("2. Player vs AI")
    print("3. View Leaderboard")
    print("4. View Game History")
    print("5. Exit")
    return input("Select an option: ").strip()


def play_round(players, stats, history, ai_mode=False):
    """
    Conducts a single round of Tic-Tac-Toe between two players or a player and the AI.

    Time Complexity:
    - Best Case: O(1) (Game ends quickly due to a win).
    - Average Case: O(9) (Full grid is utilized).
    - Worst Case: O(9) (Full grid is utilized with no winner until the last move).
    """

    board = initialize_board()
    current_turn = players[0]
    ai_player = players[1] if ai_mode else None
    winner = None

    print("\nStarting a new game! (Type 'home' to quit to the main menu.)")

    while True:
        display_board(board)

        if ai_mode and current_turn == ai_player:
            print("AI is making a move...")
            move = ai.get_ai_move(board, ai_player, players[0])
        else:
            user_input = input(f"{current_turn}, enter your move (row col, or 'home' to quit): ").strip()
            if user_input.lower() == 'home':
                print("Returning to the main menu...")
                return
            try:
                row, col = map(int, user_input.split())
                move = (row, col)
            except ValueError:
                print("Invalid input. Enter two numbers between 0 and 2.")
                continue

        if move and board[move[0]][move[1]] is None:
            board[move[0]][move[1]] = "X" if current_turn == players[0] else "O"
        else:
            print("Cell is already occupied or invalid move. Try again.")
            continue

        if check_winner(board, "X" if current_turn == players[0] else "O"):
            winner = current_turn
            print(f"\n{current_turn} wins!")
            break
        elif is_full(board):
            print("\nIt's a draw!")
            break

        current_turn = players[1] if current_turn == players[0] else players[0]

    lb.update_stats(stats, winner, players)
    gh.add_game_history(history, winner, players, ai_mode)
    display_board(board)

    if winner:
        players.append(players.popleft())  # Winner starts the next game
    else:
        players.reverse()  # Alternate the starting player if draw


def play_game():
    """
        The main game loop. Provides options for PvP, PvAI, leaderboard, and game history.

        Time Complexity:
        - Best Case: O(1) (Immediate exit or simple operation chosen).
        - Average Case: O(n) (Where `n` is the number of rounds played or entries in history/leaderboard).
        - Worst Case: O(n) (Multiple rounds and operations performed).
        """

    stats = {}
    history = []

    while True:
        option = home_screen()
        if option == "1":
            player1 = input("Enter name for Player 1 (X): ").strip().capitalize()
            player2 = input("Enter name for Player 2 (O): ").strip().capitalize()
            if player1 not in stats:
                stats[player1] = {"wins": 0, "losses": 0, "draws": 0}
            if player2 not in stats:
                stats[player2] = {"wins": 0, "losses": 0, "draws": 0}
            players = deque([player1, player2])
            play_round(players, stats, history, ai_mode=False)
        elif option == "2":
            player_name = input("Enter your name (X): ").strip()
            if player_name not in stats:
                stats[player_name] = {"wins": 0, "losses": 0, "draws": 0}
            ai_name = "AI"
            if ai_name not in stats:
                stats[ai_name] = {"wins": 0, "losses": 0, "draws": 0}
            players = deque([player_name, ai_name])
            play_round(players, stats, history, ai_mode=True)
        elif option == "3":
            leaderboard = lb.display_leaderboard(stats)
            lb.search_leaderboard(stats)
        elif option == "4":
            game_history = gh.display_game_history(history)
            gh.search_game_history(game_history)
        elif option == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please select again.")