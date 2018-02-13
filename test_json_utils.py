import sys
import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()
    games = json_data["games"]
    for gameData in games:
        game = test_data.Game()
        game.title = games[gameData]["title"]
        game.platform = test_data.Platform(games[gameData]["platform"]["name"], 
                                           games[gameData]["platform"]["launch year"])
        game.year = games[gameData]["year"]
        game_library.add_game(game)
    #Loop through the json_data
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
    #Return the completed game_library

    return game_library
