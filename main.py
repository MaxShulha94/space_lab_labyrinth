from game_elements import Labyrinth, Player
from gameplay import add_player, game_loop

if __name__ == '__main__':
    list_of_players = add_player()

    labyrinth_instance = Labyrinth()
    labyrinth_instance.make_fire()
    player_instance = Player()


    game_loop(labyrinth_instance, list_of_players)






