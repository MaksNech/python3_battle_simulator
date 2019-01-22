from models.configurations import SIMULATOR_CONFIG as CONFIG
from models.armedforces.formations.units.vehicle import Vehicle
from models.armedforces.formations.units.soldier import Soldier


class TestVehicle():

    def setup(self):
        print("setup")
        self.vehicle = Vehicle()

    def test_init(self):
        print("test_init")
        assert self.vehicle.recharge >= 1000 / CONFIG['speed_up_recharge_val'] and self.vehicle.recharge <= 2000 / \
               CONFIG[
                   'speed_up_recharge_val']
        assert len(self.vehicle.operators) > 0 and len(self.vehicle.operators) < 4
        for operator in self.vehicle.operators:
            assert isinstance(operator, Soldier)

    def test_get_operators_attack_val(self):
        print("test_get_operators_attack_val")
        list_op_attack_val = self.vehicle.get_operators_attack_val()
        assert isinstance(list_op_attack_val, list)
        for val in list_op_attack_val:
            assert val > 0
        assert len(self.vehicle.operators) == len(list_op_attack_val)

    def test_calc_operator_dmg(self):
        print("test_calc_operator_dmg")
        self.vehicle.operators = [Soldier(), Soldier()]
        self.vehicle.operators[0].health = 0
        self.vehicle.calc_operator_dmg(5.7, 0, 20)
        assert self.vehicle.operators[0].health == 0
        self.vehicle.operators[1].health = 23.4
        self.vehicle.calc_operator_dmg(12.1, 1, 10)
        assert self.vehicle.operators[1].health == 22.189999999999998
        self.vehicle.operators[0].health = 40
        self.vehicle.calc_operator_dmg(17, 0, 40)
        assert self.vehicle.operators[0].health == 33.2

    def test_to_attack(self):
        print("test_to_attack")
        assert isinstance(self.vehicle.to_attack(), float)
        assert self.vehicle.to_attack() > 0

    def test_to_damage(self):
        print("test_to_damage")
        self.vehicle.last_attack_time = self.vehicle._timer.get_current_time()
        self.vehicle.last_attack_time -= self.vehicle.recharge
        self.vehicle.operators = [Soldier(), Soldier(), Soldier()]
        self.vehicle.operators[0].experience = 6.3
        self.vehicle.operators[1].experience = 8.6
        self.vehicle.operators[2].experience = 4.5
        assert self.vehicle.to_damage() == 0.294
        self.vehicle.last_attack_time = self.vehicle._timer.get_current_time()
        self.vehicle.last_attack_time -= self.vehicle.recharge
        self.vehicle.operators[0].experience = 12.3
        self.vehicle.operators[1].experience = 34.9
        self.vehicle.operators[2].experience = 6.1
        assert self.vehicle.to_damage() == 0.633

    def test_get_damage(self):
        print("test_get_damage")
        self.vehicle.operators = [Soldier(), Soldier(), Soldier()]
        self.vehicle.operators[1].health = -1
        self.vehicle.get_damage(5.7)
        assert len(self.vehicle.operators) == 2
        self.vehicle.operators[0].health = 66
        self.vehicle.operators[1].health = 12.4
        self.vehicle.get_damage(3.3)
        assert self.vehicle.health == 57.73333333333333
        self.vehicle.operators[0].health = -2
        self.vehicle.operators[1].health = -2.4
        self.vehicle.get_damage(6.8)
        assert self.vehicle.health == -1

    def test_incrs_experience(self):
        print("test_incrs_experience")
        self.vehicle.operators=[Soldier(),Soldier()]
        self.vehicle.operators[0].experience = 44
        self.vehicle.operators[0].incrs_experience()
        assert self.vehicle.operators[0].experience == 44.01
        self.vehicle.operators[1].experience = 12.6
        self.vehicle.operators[1].incrs_experience()
        assert self.vehicle.operators[1].experience == 12.61
        self.vehicle.operators[0].experience = 50
        self.vehicle.operators[0].incrs_experience()
        assert self.vehicle.operators[0].experience == 50

    def test_new_unit(self):
        print("test_new_unit")
        assert isinstance(Vehicle.new_unit(), Vehicle)
