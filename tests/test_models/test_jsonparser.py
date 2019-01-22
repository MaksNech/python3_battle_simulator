from models.configurations import SIMULATOR_CONFIG as CONFIG
from models.jsonparser import JsonParser
from models.armedforces.formations.formed import Formed
from models.armedforces.formations.units.unitary import Unitary


class TestJsonParser():

    def setup(self):
        print('setup')
        self.jsonparser = JsonParser()

    def test_json_parse(self):
        print('test_json_parse')
        armies_list = self.jsonparser.json_parse(CONFIG['json_armies_path'])
        assert len(armies_list) >= 2
        for army in armies_list:
            assert len(army._own_formations) >= 2
            for formation in army._own_formations:
                assert type(formation) in Formed.__subclasses__()
                for unit in formation._units:
                    assert type(unit) in Unitary.__subclasses__()


