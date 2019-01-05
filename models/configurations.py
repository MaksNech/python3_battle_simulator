from random import randint, choice

SIMULATOR_CONFIG = {
    'armies_creation_way': 1,
    'json_armies_path': 'armies.json',
    'armies_amount': randint(2, 10),
    'attack_strategy': choice(['random', 'weakest', 'strongest']),
    'formations_per_army': randint(2, 10),
    'units_per_formation': randint(5, 10),
    'speed_up_recharge_val': 100,
    'display_log': False
}
