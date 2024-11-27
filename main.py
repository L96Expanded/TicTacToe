import helper as util


# Run the game
if __name__ == "__main__":
    f = open("data.json", "w")
    f.write('{"player1": "N-A", "player2": "N-A" , "playerAI": "N-A", "move": "N-A", "home_option": "N-A", "grid":"000000000", "player_search":"N-A", "game_state":"wait", "HGames":"","LBGames":""}')
    f.close()
    util.play_game()
    