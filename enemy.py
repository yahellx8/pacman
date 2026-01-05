import random
import arcade


class Enemy:
    time_to_change_direction = 0

    def __init__(self):
        direction_options = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]
        pick_new_direction = direction_options[random.randint(0, len(direction_options) - 1)]
        self.direction = pick_new_direction
        self.time_to_change_direction = random.uniform(0.3, 1.0)
        print(pick_new_direction) #debug


enemy1 = Enemy()
