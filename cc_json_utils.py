import json
import cc_data

def make_level_from_json(json_data, title):
    level = cc_data.CCLevel()
    level.level_number = json_data["num"]
    level.time = json_data["time"]
    level.num_chips = json_data["chips"]
    level.upper_layer = json_data["upper"]
    level.lower_layer = json_data["lower"]
    for fieldInt in json_data["optional fields"]:
        if fieldInt == 3:
            field = cc_data.CCMapTitleField(title)
            level.add_field(field)
            continue
        if fieldInt == 6:
            field = cc_data.CCEncodedPasswordField(json_data["password"])
            level.add_field(field)
        if fieldInt == 7:
            field = cc_data.CCMapHintField(json_data["hint"])
            level.add_field(field)
        if fieldInt == 10:
            monsters = []
            for xcoord in json_data["monsters"]:
                monsterCoord = cc_data.CCCoordinate(int(xcoord), json_data["monsters"][xcoord])
                monsters.append(monsterCoord)
            field = cc_data.CCMonsterMovementField(monsters)
            level.add_field(field)
    return level