import datetime
import algorithms as algos

# This section has the code and functionality that the game history feature is based on


def add_game_history(history, winner, players, ai_mode):
    """
        Records the game result in the history list.

        Time Complexity:
        - Best Case: O(1) (Appends to the end of the list).
        - Average Case: O(1).
        - Worst Case: O(1).
        """

    history.append({
        'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),  # Up to minutes
        'winner': "AI" if ai_mode and winner == "AI" else winner,
        'player1': players[0],
        'player2': players[1] if not ai_mode else "AI",
        'draw': winner is None
    })


# This section manages the display of all games in the history, sorted by date.

def display_game_history(history):
    """
    Displays the game history, sorted by date.

    Time Complexity:
    - Sorting History:
      - Best Case: O(n log n) (Quicksort with optimal pivot).
      - Average Case: O(n log n) (Expected performance of quicksort).
      - Worst Case: O(n^2) (Poor pivot selection in quicksort).
    - Displaying History:
      - Best Case: O(n) (Iterating through all games for printing).
      - Average Case: O(n) (Same as best case; linear iteration).
      - Worst Case: O(n) (Same as best case; linear iteration).
    """
    history = algos.quicksort(history, 'date')  # Sort games by date.

    print("\nGame History (sorted by date):")  # Display sorted games.
    for game in history:
        result = "Draw" if game['draw'] else f"{game['winner']} won"
        print(f"{game['date']} - {game['player1']} vs {game['player2']}: {result}")

    return history


def search_game_history(history):
    """
    Searches the game history for matches involving a specific player.

    Time Complexity:
    - Sorting History:
      - Best Case: O(n log n) (Quicksort on game history with optimal pivot).
      - Average Case: O(n log n) (Expected performance of quicksort).
      - Worst Case: O(n^2) (Poor pivot selection in quicksort).
    - Searching for Player:
      - Best Case: O(1) (Player found in the first game).
      - Average Case: O(n) (Linear search through the sorted history).
      - Worst Case: O(n) (Player not found after checking all games).
    """
    print("\nSearch for a game in the history.")
    player_name = input("Enter the player's name (case-insensitive): ").strip().capitalize()

    sorted_history = algos.quicksort(history, 'date')  # Sort games by date.

    found_games = []
    for game in sorted_history:  # Linear search to find games involving the player.
        if player_name.lower() in [game['player1'].lower(), game['player2'].lower()]:
            found_games.append(game)

    if found_games:  # Output the found games.
        print(f"\nGames involving '{player_name}':")
        for game in found_games:
            result = "Draw" if game['draw'] else f"{game['winner']} won"
            print(f"{game['date']} - {game['player1']} vs {game['player2']}: {result}")
    else:
        print("No games found involving that player.")
