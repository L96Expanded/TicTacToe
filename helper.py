from collections import deque
import ai
import leaderboard as lb
import gamehist as gh
import time
import json

def change_val(key,val):
    with open('data.json') as f:
        data = json.load(f)

    data[key] = val

    with open('data.json', 'w') as f:
        json.dump(data, f)
        
def giveGridChange(ai_mode, move, turn, players):
    grid = json.load(open('data.json'))["grid"]
    if(ai_mode == False):
        move_str = json.load(open('data.json'))["move"]
        
    else:
        move_str = str(move[0]) + " " + str(move[1])
    n = (int(move_str[0]) * 3) + int(move_str[2])
    if(turn == players[0]):
        grid = grid[: n] + "1" + grid[n+1 :]
    else:
        grid = grid[: n] + "2" + grid[n+1 :]
    return grid

# Initialize the board as a 2D array
def initialize_board():
    return [[None for _ in range(3)] for _ in range(3)]


# Display the board
def display_board(board):
    print("\n".join([" | ".join([cell or " " for cell in row]) for row in board]))
    print("-" * 9)


# Check if a player has won (Row, Column, and Diagonal Traversal)
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


# Check if the board is full
def is_full(board):
    return all(all(cell is not None for cell in row) for row in board)

def home_screen():
    print("\nWelcome to Tic-Tac-Toe!")
    print("1. Player vs Player")
    print("2. Player vs AI")
    print("3. View Leaderboard")
    print("4. View Game History")
    print("5. Exit")
    while json.load(open('data.json'))["home_option"] == "N-A":
        time.sleep(0.5)
    return json.load(open('data.json'))["home_option"]
    # return json.load(open('infoTransport.json'))[0]["home_option"]


# Play a single round of the game
def play_round(players, stats, history, ai_mode=False):
    board = initialize_board()
    current_turn = players[0]
    ai_player = players[1] if ai_mode else None
    winner = None

    print("\nStarting a new game! (Type 'home' to quit to the main menu.)")

    while True:
        display_board(board)
        change_val("game_state","wait")
        if ai_mode and current_turn == ai_player:
            print("AI is making a move...")
            move = ai.get_ai_move(board, ai_player, players[0])
            gridchange = giveGridChange(True, move, current_turn, players)
            change_val("grid",gridchange)
            change_val("move","N-A")
        else:
            while json.load(open('data.json'))["move"] == "N-A":
                time.sleep(0.05)
            gridchange = giveGridChange(False, 0,current_turn, players)
            change_val("grid",gridchange)
            user_input = json.load(open('data.json'))["move"]
            change_val("move","N-A")
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
            change_val("grid","000000000")
            change_val("home_option","N-A")
            
            change_val("game_state","finish")
            break
        elif is_full(board):
            print("\nIt's a draw!")
            change_val("grid","000000000")
            change_val("home_option","N-A")
            
            change_val("game_state","finish")
            break

        current_turn = players[1] if current_turn == players[0] else players[0]

    lb.update_stats(stats, winner, players)
    gh.add_game_history(history, winner, players, ai_mode)
    display_board(board)

    if winner:
        players.append(players.popleft())  # Winner starts the next game
    else:
        players.reverse()  # Alternate the starting player if draw

# Main game loop
def play_game():
    stats = {}
    history = []

    while True:
        option = home_screen()
        if option == "1":
            print("Enter name for Player 1 (X): ")
            while json.load(open('data.json'))["player1"] == "N-A" or json.load(open('data.json'))["player2"] == "N-A":
                time.sleep(0.5)
            player1 = json.load(open('data.json'))["player1"]
            player2 = json.load(open('data.json'))["player2"]
            if player1 not in stats:
                stats[player1] = {"wins": 0, "losses": 0, "draws": 0}
            if player2 not in stats:
                stats[player2] = {"wins": 0, "losses": 0, "draws": 0}
            players = deque([player1, player2])
            play_round(players, stats, history, ai_mode=False)
        elif option == "2":
            while json.load(open('data.json'))["player1"] == "N-A":
                time.sleep(0.5)
                
            player_name = json.load(open('data.json'))["player1"]
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