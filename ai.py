import helper as util

# This file stores all the necessary functions which make the AI features work


# Greedy AI Move Logic
def greedy_ai_move(board, ai_player, human_player):
    """
        Determines the AI's next move using a greedy strategy:
        1. Prioritize winning moves.
        2. Block the opponent's winning moves.
        3. Choose the center if available.
        4. Choose a corner or edge strategically.
        5. Fallback to the first available move.

        Time Complexity:
        - Best Case: O(1) (Immediate win or block is found on the first iteration).
        - Average Case: O(9) (Iterates over the entire 3x3 grid once).
        - Worst Case: O(9) (Checks all cells before deciding).
        """

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


def get_ai_move(board, ai_player, human_player):
    """
        Wrapper for calling the greedy AI move function.
        Directs the AI to use the greedy algorithm.

        Time Complexity:
        - Best Case: O(1) (Immediate win or block is found on the first iteration).
        - Average Case: O(9) (Iterates over the entire 3x3 grid once).
        - Worst Case: O(9) (Checks all cells before deciding).
        """
    return greedy_ai_move(board, ai_player, human_player)