import algorithms as algos


# This section manages the leaderboard, including displaying it and searching for player statistics.

def update_stats(stats, winner, players):
    """
        Updates the leaderboard statistics for the players after a match.

        Time Complexity:
        - Best Case: O(1) (Direct dictionary operations).
        - Average Case: O(1).
        - Worst Case: O(1).
        """

    if winner:
        stats[winner]['wins'] += 1
        for player in players:
            if player != winner:
                stats[player]['losses'] += 1
    else:
        for player in players:
            stats[player]['draws'] += 1


def display_leaderboard(stats):
    """
    Displays the leaderboard sorted by the number of wins in descending order.

    Time Complexity:
    - Best Case: O(n log n) (Sorting leaderboard with quicksort).
    - Average Case: O(n log n) (Expected performance of quicksort).
    - Worst Case: O(n^2) (Quicksort with poor pivot selection).
    """
    leaderboard = [{'name': player, **stats[player]} for player in stats]
    leaderboard = algos.quicksort(leaderboard, 'wins')

    print("\nLeaderboard (sorted by wins):")
    for i, player in enumerate(leaderboard, 1):
        print(f"{i}. {player['name']} - Wins: {player['wins']}, Losses: {player['losses']}, Draws: {player['draws']}")
    return leaderboard


def search_leaderboard(stats):
    """
    Searches for a specific player's stats in the leaderboard by name.

    Time Complexity:
    - Best Case: O(1) (Player is found in the first comparison).
    - Average Case: O(n) (Linear search through the leaderboard).
    - Worst Case: O(n) (Player is not found after checking all entries).
    """
    print("\nSearch for a player in the leaderboard.")
    name = input("Enter the player's name: ").strip()

    leaderboard = [{'name': player, **stats[player]} for player in stats]

    for player in leaderboard:
        if player['name'].lower() == name.lower():
            print(f"Player {player['name']} - Wins: {player['wins']}, Losses: {player['losses']}, Draws: {player['draws']}")
            return

    print("Player not found.")
