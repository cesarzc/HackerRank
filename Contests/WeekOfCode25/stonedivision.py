#!/bin/python3

import copy

class GameNode:
    def __init__(self, player, stone_piles, divisor_set):
        self.player = player
        self.stone_piles = stone_piles
        self.divisor_set = divisor_set

    #!/bin/python3

import copy

class Game:
    divisors = []

class Position:
    def __init__(self, player, stone_piles):
        self.player = player
        self.stone_piles = stone_piles

    @staticmethod
    def create_position_from_pile_size_and_divisor(position, pile_size, divisor):
        pile_size_key = str(pile_size)
        piles_count = position.stone_piles[pile_size_key]
        new_pile_size = int(pile_size_key) // divisor
        new_pile_size_key = str(new_pile_size)
        new_stone_piles = copy.deepcopy(position.stone_piles)
        if new_pile_size_key in new_stone_piles:
            new_stone_piles[new_pile_size_key] += divisor
        else:
            new_stone_piles[new_pile_size_key] = divisor

        if piles_count > 1:
            new_stone_piles[pile_size_key] -= 1
        else:
            new_stone_piles.pop(pile_size_key, None)

        new_player = (position.player + 1) % 2
        new_position = Position(new_player, new_stone_piles)
        return new_position

    def is_losing_position(self):
        for pile_size_key in self.stone_piles.keys():
            pile_size = int(pile_size_key)
            for divisor in Game.divisors:
                if (pile_size % divisor) == 0:
                    return False

        return False

    def get_next_positions(self):
        positions = []
        for pile_size_key in self.stone_piles.keys():
            pile_size = int(pile_size_key)
            for divisor in Game.divisors:
                if (pile_size % divisor) == 0:
                    position =\
                        Position.create_position_from_pile_size_and_divisor (\
                            self, pile_size, divisor)

                    positions.append(position)

        return positions

pile_size_str, set_size_str = input().split(' ')
initial_stone_piles = {}
initial_stone_piles[pile_size_str] = 1
Game.divisors = [int(item) for item in input().strip().split(' ')]
Game.divisors.sort(reverse=True)
initial_position = Position(1, initial_stone_piles)
positions_stack = [initial_position]
player_one_winner_exists = False
while (len(positions_stack) > 0) and (not player_one_winner_exists):
    player_one_position = positions_stack.pop()
    player_two_positions = player_one_position.get_next_positions()
    for player_two_position in player_two_positions:
        if player_two_position.is_losing_position():
            player_one_winner_exists = True
            break
        else:
            positions_stack.extend(player_two_position.get_next_positions())

if player_one_winner_exists:
    print("First")
else:
    print("Second")
