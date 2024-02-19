
from game_elements import Player
from text_generators import attack_info_input



def add_player():
    # Добавляет игроков в игру
    list_of_players = []
    quantity = input('How many players? ')
    if quantity.isdigit():
        quantity = int(quantity)
        for _ in range(quantity):
            name = input('Enter your name: ')
            list_of_players.append(Player(name=name))
    else:
        print('Invalid! Enter correct number of players')
    return list_of_players





def players_turn(player, labyrinth, list_of_players, attempts=3):

    while attempts != 0:
        other_players = [other_player for other_player in list_of_players if other_player.name != player.name]
        for _ in other_players:
            if _.name != player.name and _.location == player.location:
                users_input = attack_info_input(player, other_players)

                if users_input == "MOVE":
                    player.move(labyrinth)

                    return

                players_names = [p.name for p in list_of_players]
                if users_input in players_names:
                    target_player = [player for player in list_of_players if player.name
                                     == users_input][0]
                    player.attack_player(target_player)
                    print(f'{player.name} damaged {target_player.name}, {target_player.health} health points left')
                    return


                print(f"Wrong input, try again. {attempts} tries left!")
                attempts -= 1
            # player.move(labyrinth)

    print("You did nothing, try next time!")


def game_loop(labyrinth, players_list):

    if len(players_list) == 0:
        print('Game over.')
        return

    for player in players_list:
        print(f'Player {player.name} is active!')
        players_turn(player, labyrinth, players_list)

        if player.health == 0:
            print("Game over for player ", player.name)
            players_list = [p for p in players_list if p != player]

    game_loop(labyrinth, players_list)
