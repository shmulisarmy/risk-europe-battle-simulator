"""this file is used for simulating many games"""

from collections import defaultdict
from copy import deepcopy

from player import Player
from battle import Battle




simulate_round_times: int = 10000


player_1_troops = {
    "footman": 28,
    "archer": 8,
    "knight": 6,
    "siege": 3,
}

player_2_troops = {
    "footman": 43,
    "archer": 6,
    "knight": 7,
    "siege": 1,
}


player_1 = Player("shmuli the adventurer", player_1_troops)
player_2 = Player("mendel the mage", player_2_troops)


winners = defaultdict(int)

print(f"simulate {simulate_round_times} rounds...")

for _ in range(simulate_round_times//2):
    current_attacker: Player = deepcopy(player_1)
    current_defender: Player = deepcopy(player_2)

    battle = Battle(current_attacker, current_defender)
    battle.start(attacker=current_attacker, defender=current_defender)
    winners[battle.winner.name] += 1

for _ in range(simulate_round_times//2):
    current_attacker: Player = deepcopy(player_2)
    current_defender: Player = deepcopy(player_1)

    battle = Battle(current_attacker, current_defender)
    battle.start(attacker=current_attacker, defender=current_defender)
    winners[battle.winner.name] += 1



for winner, times in winners.items():
    print(f"{winner} won {times} times")