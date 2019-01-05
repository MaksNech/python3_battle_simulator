import json
# USED modules for factories: #############################
from .armedforces.formations.units.vehicle import Vehicle
from .armedforces.formations.units.soldier import Soldier
from .armedforces.formations.squad import Squad
from .armedforces.army import Army


##########################################################

class JsonParser:

    def json_parse(self, file_path: str) -> list:
        """
        Create armies from json file
        :param file_path: (str)
        :return: (list)
        """
        armies_list = []
        formations_list = []
        units_list = []
        with open(file_path) as json_file:
            data = json.load(json_file)
            for army in data['armies_list']:
                for formation in army['formations_list']:
                    for unit in formation['units_list']:
                        try:
                            units_list.append(eval(unit['class']).new_unit())
                        except:
                            continue
                    try:
                        my_formation = eval(formation['class']).new_formation()
                        my_formation._units = units_list
                        units_list = []
                        formations_list.append(my_formation)
                    except:
                        continue
                try:
                    my_army = eval(army['class']).new_army()
                    my_army._own_formations = formations_list
                    formations_list = []
                    armies_list.append(my_army)
                except:
                    continue

        return armies_list
