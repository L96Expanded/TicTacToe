import helper as util


# --- AI Logic ---

# Minimax algorithm for AI moves
def minimax(board, depth, is_maximizing, ai_player, human_player):
    if util.check_winner(board, ai_player):
        return 10 - depth
    if util.check_winner(board, human_player):
        return depth - 10
    if util.is_full(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    board[i][j] = ai_player
                    score = minimax(board, depth + 1, False, ai_player, human_player)
                    board[i][j] = None
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    board[i][j] = human_player
                    score = minimax(board, depth + 1, True, ai_player, human_player)
                    board[i][j] = None
                    best_score = min(best_score, score)
        return best_score


# Get the best AI move
def get_ai_move(board, ai_player, human_player):
    best_score = float('-inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                board[i][j] = ai_player
                score = minimax(board, 0, False, ai_player, human_player)
                board[i][j] = None
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move