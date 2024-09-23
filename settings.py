special_attack_order = ["siege", "archer", "knight"]


special_attack_kind = {
    "siege": {
        "on roll": 3,
        "max strike count": 2,
    },
    "archer": {
        "on roll": 5,
        "max strike count": 1,
    },
    "knight": {
        "on roll": 3,
        "max strike count": 1,
    },
}

troop_value: dict = {
    "footman": 1,
    "archer": 2,
    "knight": 5,
    "siege": 10,
}

troop_ranking_reversed = ["footman", "archer", "knight", "siege"]

