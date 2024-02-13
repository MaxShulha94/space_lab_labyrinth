from const import ATTEMPTS

from main import cell_instance, player_instance


# def players_turn(player, cell):
#     current_player = player.players
#     print(current_player)
#     # current_player.active = True
#     # while current_player.active:




def game_loop(cell):

    for player_name, player_info in cell.players.items():
        current_player = player_instance.players[player_name]
        current_player.active = True
        print(current_player)

        # if player_info.active is True and player_info.health > 0:
        #     print(f'{player_info.name} is active!')
        #     self.to_hit_players()



# if cell_instance.players[player_name] is False:
#     print(f'{player_info.name}')


# current_player.active = False
# else:
#     print(f'{player_info.name} has {player_info.health} points of health. Game over!')
#     del cell_instance.players[player_name]
# current_player.active = False


# def users_action_input(other_players):
#     pass
#
#
# def players_turn(player, labyrinth, players_dict):
#     try_counter = Try(total_tries=3)
#
#     while ATTEMPTS != 0:
#         other_players =
#         users_input = users_action_input(other_players)
#
#         if users_input == "MOVE":
#             player.move_player(labyrinth, other_players)
#             return
#
#         players_names = [p.name for p in players_list]
#         if users_input in players_names:
#             target_player = [player for player in players_list if player.name
#                              == users_input][0]
#             player.punch(target_player)
#             return
#
#         print(f"Wrong input, try again. {try_counter.num} tries left!")
#         try_counter.decrease_try_number()
#
#     print("You did nothing, try next time!")


def game_loop(labyrinth, players):
    # if len(players_list) == 1:
    if players.location == [7, 3] and players.items['key'] is True:
        print(f"Player {players.name} won! Game is over.")
        return

    # round
    for player in cell_instance.players.keys():
        print(f"Player {player}")
    #     print(f"###\nPlayer {player.name} is active!\n###")
    #     players_turn(player, labyrinth, players_list)
    #
    #     if player.health == 0:
    #         print("Game over for player ", player.name)
    #         players_list = [p for p in players_list if p != player]
    #
    # game_loop(labyrinth, players_list)
