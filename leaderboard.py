import algorithms as algos
import helper as help
import time
import json


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
    help.change_val("LBGames",leaderboard)
    
    print("\nLeaderboard (sorted by wins):")
    for i, player in enumerate(leaderboard, 1):
        print(f"{i}. {player['name']} - Wins: {player['wins']}, Losses: {player['losses']}, Draws: {player['draws']}")
    return leaderboard


# Search for a specific player's stats
# Search for players in the leaderboard
# Search leaderboard by name
def search_leaderboard(stats):
    print("\nSearch for a player in the leaderboard.")
    while json.load(open('data.json'))["player_search"] == "N-A":
        time.sleep(0.5)
    name = json.load(open('data.json'))["player_search"]  # Take input as-is
    if json.load(open('data.json'))["player_search"] == "NONE":
        help.change_val("home_option","N-A")
    help.change_val("player_search","N-A")
    
    
    # Convert stats dictionary into a list for searching
    leaderboard = [{'name': player, **stats[player]} for player in stats]

    # Find player using linear search (case-insensitive)
    for player in leaderboard:
        if player['name'].lower() == name.lower():  # Compare names case-insensitively
            print(f"Player {player['name']} - Wins: {player['wins']}, Losses: {player['losses']}, Draws: {player['draws']}")
            return
    print("Player not found.")