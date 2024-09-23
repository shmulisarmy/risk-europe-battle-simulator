from random import randint
from settings import troop_ranking_reversed, troop_value
from utils import colors, average, next_or_none


class Player:
    all_instances = []
    def __init__(self, name, troops):
        self.name = name
        self.troops: dict = troops
        self.in_battle: bool = False
        self.attacking_position = None
        self.in_battle_with: 'Player'|None = None

        self.all_rolls: list = []

        Player.all_instances.append(self)

    def toString(self):
        return f"{self.name}: {self.troops}"
    
    def display(self):
        print(self.toString())
    
    def lose_troops(self, troops_left_to_lose: int) -> bool:
        """returns True if the player was able to lose the required number of troops"""
        ran_out_out_troops = False
        troop_ranking_reversed_iter = iter(troop_ranking_reversed)
        while troops_left_to_lose:
            current_troop = next_or_none(troop_ranking_reversed_iter)
            if not current_troop:
                ran_out_out_troops = True
                break
            troops_able_to_be_lost: int = min(self.troops[current_troop], troops_left_to_lose)


            print(f"{self.name} lost {troops_able_to_be_lost} {current_troop}'s")
            self.troops[current_troop] -= troops_able_to_be_lost
            troops_left_to_lose -= troops_able_to_be_lost

        if ran_out_out_troops:
            #was not able to lose the required number of troops
            return False

        return True


    def start_battle(self, other_player: 'Player'):
        self.in_battle = True
        self.attacking_position = "attacker"
        other_player.in_battle = True
        other_player.attacking_position = "defender"

        self.in_battle_with = other_player
        other_player.in_battle_with = self

    @classmethod
    def display_all(cls):
        for player in cls.all_instances:
            player.display()

    def roll_dice(self):
        dice_roll: int = randint(1, 6)
        self.all_rolls.append(dice_roll)
        incode_color: function = colors[dice_roll-1]
        print(f"{self.name} rolled {incode_color(dice_roll)}")
        return dice_roll
    
    def has_troops(self):
        return any(self.troops.values())
    
    def is_probably_a_cheater(self):
        return average(self.all_rolls) >= 5.2
    
    def get_players_troop_value(self) -> int:
        total_troop_value: int = 0
        for troop, amount in self.troops.items():
            total_troop_value += amount * troop_value[troop]

        return total_troop_value

    
    def __gt__(self, other: 'Player'):
        return self.get_players_troop_value() > other.get_players_troop_value()


    def get_troop_count(self) -> int:
        return sum(self.troops.values())
