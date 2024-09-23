from player import Player
from settings import special_attack_order, special_attack_kind
from utils import red, green, yellow, blue, magenta, cyan



class Battle:
    def __init__(self, player_1: Player, player_2: Player):
        self.player_1 = player_1
        self.player_2 = player_2
        self.fighting_players = [player_1, player_2]
        self.active: bool = False
        self.attacker: Player|None = None
        self.defender: Player|None = None
        self.round_upto: int = 0
        self.winner: Player|None = None


    def __contains__(self, player: Player):
        return player in self.fighting_players

    def start(self, attacker: Player, defender: Player):
        assert self.__contains__(attacker)
        assert self.__contains__(defender)

        self.active = True

        self.attacker = attacker
        self.defender = defender
        attacker.start_battle(defender)

        self()
    def end(self, winner: Player):
        # print(f"\n***************** {winner.name} wins *****************\n")
        self.winner = winner
        self.active = False
        self.attacker = None
        self.defender = None


    def regular_part_of_round(self) -> bool:
        attackers_dice_count: int = min(self.attacker.get_troop_count(), 3)
        defenders_dice_count: int = min(self.attacker.get_troop_count(), 2)

        attackers_dice_rolls = sorted([self.attacker.roll_dice() for _ in range(attackers_dice_count)])
        defenders_dice_rolls = sorted([self.defender.roll_dice() for _ in range(defenders_dice_count)])

        dice_match_amount: int = min(attackers_dice_count, defenders_dice_count)

        for i in range(dice_match_amount):
            #tie goes to defender
            if attackers_dice_rolls[i] > defenders_dice_rolls[i]:
                if not self.defender.lose_troops(1):
                    return False
            else:
                if not self.defender.lose_troops(1):
                    return False
                

        return True

    def special_attackers_part_of_round(self) -> bool:
        for current_attacking_troop in special_attack_order:
            number_needed_to_attack: int = special_attack_kind[current_attacking_troop]["on roll"]
            # print(red(f"\n***************** {current_attacking_troop} attacking *****************\n"))
            # print(yellow(f"a {number_needed_to_attack} or higher roll is needed to attack"))
            for current_attacking_player in self.fighting_players:
                # print(f"\n{current_attacking_player.name} is attacking with {current_attacking_player.troops[current_attacking_troop]} {current_attacking_troop}'s\n")
                current_attacking_player: Player
                troop_dice_roll_amount: int = special_attack_kind[current_attacking_troop]["max strike count"]
                total_troop_dice_roll_amount: int = troop_dice_roll_amount*current_attacking_player.troops[current_attacking_troop]


                troop_attack_opertunity: int = sum([current_attacking_player.roll_dice() >= number_needed_to_attack for _ in range(total_troop_dice_roll_amount)])

                if not current_attacking_player.in_battle_with.lose_troops(troop_attack_opertunity):
                    return False
                
        return True
                
    def round(self) -> bool:
        self.display()

        completed: bool = self.special_attackers_part_of_round()
        if not completed:
            return False
            
        completed = self.regular_part_of_round()
        if not completed:
            return False
        
        return True
        
    def __call__(self):
        # print(f"\n***************** {self.player_1.name} vs {self.player_2.name} *****************\n")
        while self.player_1.has_troops() and self.player_2.has_troops():
            self.round_upto += 1
            self.round()


        if self.player_1.has_troops():
            self.end(winner=self.player_1)
        else:
            self.end(winner=self.player_2)


    def test_status_sync(self):
        """even if false is returned, it could be do to the\n
        fact that a status transition is happening now \n
        and not a logic error""" 

        if self.active:
            if not self.attacker:
                return False

            if not self.defender:
                return False
        else:
            if self.attacker or self.defender:
                return False
            
        return True


    def display(self):
        if self.active:
            # print(f"\n***************** round {self.round_upto} *****************\n")

            # print("Attacker: ", end="")
            self.attacker.display()
            # print("Defender: ", end="")
            self.defender.display()
        elif self.winner:
            pass
            # print(f"{self.winner.name} wins")
        else:
            # print("Battle has not started yet")
            pass


   

        



   
