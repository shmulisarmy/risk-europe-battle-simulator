from player import Player
from settings import special_attack_order, special_attack_kind
from utils import red, green, yellow, blue, magenta, cyan
from battle import Battle






player_1_troops = {
    "footman": 28,
    "archer": 2,
    "knight": 3,
    "siege": 1,
}

player_2_troops = {
    "footman": 43,
    "archer": 6,
    "knight": 7,
    "siege": 1,
}


player_1 = Player("shmuli the adventurer", player_1_troops)
player_2 = Player("mendel the mage", player_2_troops)


battle = Battle(player_1, player_2)
battle.start(attacker=player_1, defender=player_2)
