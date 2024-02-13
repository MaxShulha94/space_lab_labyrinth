from game_elements import Labyrinth, Player, Cell
from gameplay import game_loop

if __name__ == '__main__':
    labyrinth_instance = Labyrinth()
    labyrinth_instance.generate_labyrinth()

    player_instance = Player()
    players_dict = player_instance.add_player()


    cell_instance = Cell(labyrinth=labyrinth_instance, players=players_dict)
    game_loop(cell_instance)








