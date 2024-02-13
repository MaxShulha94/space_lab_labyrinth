def move_info_input(attempts, player_name):
    return input(f'''
{player_name} ,where would you like to move?
You have {attempts} chances for correct input:
UP to move up,
DOWN to move down,
LEFT to move left,
RIGHT to move right
''')


def attack_info_input(other_players):
    return input(f'''
You can hit {other_players} for 1 damage and finish your move, or skip hit and move to another cell.
If you want to hit player - enter player`s name.
If you want to move - enter MOVE.
''')