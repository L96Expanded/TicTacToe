import algorithms as algos


def update_stats(stats, winner, players):
    if winner:
        stats[winner]['wins'] += 1
        for player in players:
            if player != winner:
                stats[player]['losses'] += 1
    else:
        for player in players:
            stats[player]['draws'] += 1


# Display leaderboard
def display_leaderboard(stats):
    leaderboard = [{'name': player, **stats[player]} for player in stats]
    leaderboard = algos.quicksort(leaderboard, 'wins')  # Sort descending by wins

    print("\nLeaderboard (sorted by wins):")
    for i, player in enumerate(leaderboard, 1):
        print(f"{i}. {player['name']} - Wins: {player['wins']}, Losses: {player['losses']}, Draws: {player['draws']}")
    return leaderboard


# Search for a specific player's stats
# Search for players in the leaderboard
# Search leaderboard by name
def search_leaderboard(stats):
    print("\nSearch for a player in the leaderboard.")
    name = input("Enter the player's name: ").strip()  # Take input as-is

    # Convert stats dictionary into a list for searching
    leaderboard = [{'name': player, **stats[player]} for player in stats]

    # Find player using linear search (case-insensitive)
    for player in leaderboard:
        if player['name'].lower() == name.lower():  # Compare names case-insensitively
            print(f"Player {player['name']} - Wins: {player['wins']}, Losses: {player['losses']}, Draws: {player['draws']}")
            return
    print("Player not found.")