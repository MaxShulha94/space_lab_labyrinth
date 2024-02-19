def move_info_input(attempts, player_name):
    return input(f'''
{player_name} ,where would you like to move?
You have {attempts} chances for correct input:
UP to move up,
DOWN to move down,
LEFT to move left,
RIGHT to move right
''')


def attack_info_input(player, other_players):
    neighbours = [other_player for other_player in other_players if other_player.location == player.location ]

    players_list_string = ", ".join([player.name for player in neighbours])
    return input(f'''
You can hit {players_list_string} for 1 damage and finish your move, or skip hit and move to another cell.
If you want to hit player - enter player`s name.
If you want to move - enter MOVE.
''')
