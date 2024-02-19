import json

import random


from const import DIRECTIONS_LIST, DIRECTIONS


from text_generators import move_info_input


class Labyrinth:
    def __init__(self, labyrinth: dict = None):
        with open('labyrinth_map.json', 'r') as json_file:
            self.labyrinth = json.load(json_file)



    def make_fire(self):
        # Генерирует в 5-ти случайных ячейках пламя
        fire_counter = 0
        while fire_counter < 4:
            random_key = random.choice(list(self.labyrinth.keys()))
            current_cell = self.labyrinth[random_key]
            if current_cell.get('objects') is not None:
                continue
            current_cell['objects'] = {'fire': 1}
            fire_counter += 1

        return self.labyrinth

    def remove_fire(self):
        # Удаляет пламя из ячеек в конце круга
        for key, cell in self.labyrinth.items():
            if cell['objects'] == {'fire': 1}:
                del cell['objects']

        return self.labyrinth


class Player:
    def __init__(self, name: str = '', x: int = 0, y: int = 0, active: bool = False,
                 health: int = 5, items: dict = None):
        self.name = name
        self.active = active
        self.location = [x, y]
        self.health = health
        self.items = {}



    def work_with_objects(self, labyrinth, players_list):

        for _ in labyrinth.labyrinth.items():


            if self.location[0] == _[1]['x'] and self.location[1] == _[1]['y'] and _[1]['objects'] is not None:

                if _[1]['objects'] == {'fire': 1}:
                    self.health -= 1
                    print(f'{self.name} gets in fire, {self.health} points left.')

                if _[1]['objects'] == {"heart": 1}:
                    self.health = 5
                    print(f'{self.name} feels better! Health is {self.health}.')

                if _[1]['objects'] == {"key": 1}:
                    self.items.update({"key": 1})
                    _[1]['objects'].pop('key')
                    print(f'{self.name} got key! {self.items}')

                if _[1]['objects'] == {"Golem": 1}:
                    if self.items == {"key": 1}:
                        print(f'***** {self.name} wins this game! Congratulations! *****')
                    else:
                        print(f'{self.name} was killed by Golem!')
                        players_list = [p for p in players_list if p != self.player]







    def move(self, labyrinth):
        cell_location = [[labyrinth.labyrinth[cell]['x'], labyrinth.labyrinth[cell]['y']] for cell in labyrinth.labyrinth]
        attempts = 3
        while attempts != 0:
            move_direction = move_info_input(attempts, self.name)


            if move_direction not in DIRECTIONS_LIST:
                attempts -= 1
                print(f"Wrong input! {attempts} attempts left.")


            if move_direction in DIRECTIONS_LIST:
                dx, dy = DIRECTIONS[move_direction]
                self.location[0] += dx
                self.location[1] += dy

                for cell in cell_location:
                    if self.location[0] == cell[0] and self.location[1] == cell[1]:
                        print(f"Moved {move_direction} to {self.location}")
                        return

                else:
                    dx, dy = DIRECTIONS[move_direction]
                    self.location[0] -= dx
                    self.location[1] -= dy
                    self.health -= 1

                print(
                    f"Wrong vector! {self.name} get 1 damage, {self.health} points left. Current location: {self.location}")
                return
        if attempts == 0:
            print("Too many wrong inputs. Next player to make " "action.")
            return



    def attack_player(self, target_player):
        target_player.health -= 1
        return f'{target_player.name} lost 1 health point. {target_player.health} health points left'





        # print(f'{player.name} was removed from game!')
        # print(f'len after={len(players_list)}')