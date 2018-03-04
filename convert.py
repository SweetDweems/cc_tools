import cc_dat_utils
import cc_json_utils
import cc_data
import test_json_utils
import json

#Part 1
#Use cc_data_utils.make_cc_data_from_dat() to load pfgd_test.dat
#print the resulting data
def convert_dat(dat_file="data/pfgd_test.dat"):
    print(cc_dat_utils.make_cc_data_from_dat(dat_file))


#Part 2
input_json_file = "test_data.json"
def gameLibrary(json_file = "test_data.json"):
    with open(json_file, "r") as reader:
        gameData = json.load(reader)
    print(test_json_utils.make_game_library_from_json(gameData))

### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print_game_library(game_library_data) in test_data.py
### End Add Code Here ###


#Part 3
#Load your custom JSON file
#Convert JSON data to cc_data
#Save converted data to DAT file
input_json_file = "dweems_cc1.json"
def makeDatFromJson(json_file="dweems_cc1.json", datFileName="dweems_cc1.dat"):
    levelPack = cc_data.CCDataFile()
    with open(json_file, "r") as reader:
        levels = json.load(reader)
    for levelData in levels["Levels"]:
        level = cc_json_utils.make_level_from_json(levels["Levels"][levelData], levelData)
        levelPack.add_level(level)
    cc_dat_utils.write_cc_data_to_dat(levelPack, datFileName)

#makeDatFromJson(input_json_file, "dweems_cc1.dat")