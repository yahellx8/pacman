import random
import arcade


class Enemy:
    time_to_change_direction = 0

    def __init__(self):
        pick_new_direction = random.randint(1, 3)
        self.direction = pick_new_direction
        print(pick_new_direction)


Enemy()