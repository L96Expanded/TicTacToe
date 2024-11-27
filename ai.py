import helper as util


# --- AI Logic ---

# Greedy AI Move Logic
def greedy_ai_move(board, ai_player, human_player):
    # 1. Check for a winning move
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                board[i][j] = ai_player
                if util.check_winner(board, ai_player):
                    board[i][j] = None  # Undo the move
                    return (i, j)  # Take the winning move
                board[i][j] = None  # Undo the move

    # 2. Block the opponent's winning move
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                board[i][j] = human_player
                if util.check_winner(board, human_player):
                    board[i][j] = None  # Undo the move
                    return (i, j)  # Block the opponent's win
                board[i][j] = None  # Undo the move

    # 3. Take the center if available
    if board[1][1] is None:
        return (1, 1)

    # 4. Take one of the corners
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    for corner in corners:
        if board[corner[0]][corner[1]] is None:
            return corner

    # 5. Take one of the edges
    edges = [(0, 1), (1, 0), (1, 2), (2, 1)]
    for edge in edges:
        if board[edge[0]][edge[1]] is None:
            return edge

    # 6. Fallback to the first available move (should rarely happen)
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                return (i, j)


# Get the best AI move
# Get the best AI move using the Greedy Algorithm
def get_ai_move(board, ai_player, human_player):
    # Use the greedy_ai_move function logic to make the decision
    return greedy_ai_move(board, ai_player, human_player)


