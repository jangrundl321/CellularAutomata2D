import random

import numpy as np

from CellularAutomataBlock2D import CellularAutomataBlock2D as CA

STREET = 0
YOUNG_TREE = 1
GROWING_TREE = 2
TREE = 3
WEAK_FIRE = 4
BURNING_FIRE = 5
NEW_FIRE = 6

WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
BLOCK_SIZE = 5
REFRESH_TIME = 10

NUMBER_OF_TREE_TILES = 100
NUMBER_OF_STREET_TILES = 30
NUMBER_OF_NEW_FIRE_TILES = 10

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREY = (211, 211, 211)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
BROWN = (255, 248, 220)
GREEN = (0, 255, 0)
LIGHT_GREEN = (144, 238, 144)
DARK_GREEN = (0, 100, 0)

ALPHA = 0.01
BETA = 0.3
DELTA = 0.000005
class ExtendedForestFireCA(CA):

    def __init__(self):
        name = "Extended Forest Fire CA"
        neighborhood = 0
        states_and_colors = [(STREET, GREY), (YOUNG_TREE, LIGHT_GREEN), (GROWING_TREE, GREEN), (TREE, DARK_GREEN),
                             (WEAK_FIRE, YELLOW), (BURNING_FIRE, ORANGE), (NEW_FIRE, RED)]
        initial_state_grid = self.generate_initial_state_grid()
        super().__init__(name, neighborhood, states_and_colors, initial_state_grid)

    def generate_initial_state_grid(self):
        grid = np.ones((WINDOW_HEIGHT, WINDOW_WIDTH))

        for i in range(NUMBER_OF_NEW_FIRE_TILES):
            random_col = np.random.randint(0, WINDOW_WIDTH)
            random_row = np.random.randint(0, WINDOW_HEIGHT)
            grid[random_row, random_col] = NEW_FIRE

        for i in range(NUMBER_OF_STREET_TILES):
            random_col = np.random.randint(0, WINDOW_WIDTH)
            random_row = np.random.randint(0, WINDOW_HEIGHT)
            grid[random_row, random_col] = STREET

        for i in range(NUMBER_OF_TREE_TILES):
            random_col = np.random.randint(0, WINDOW_WIDTH)
            random_row = np.random.randint(0, WINDOW_HEIGHT)
            grid[random_row, random_col] = TREE

        return grid

    def update(self):
        current_grid = self.current_state_grid
        new_grid = np.zeros((current_grid.shape[0], current_grid.shape[1]))

        for row, col in np.ndindex(current_grid.shape):
            neighborhood = self.get_neighborhood(row, col)
            counter_fire_in_neighborhood = 0

            for x in neighborhood:
                if current_grid[x] == NEW_FIRE or current_grid[x] == WEAK_FIRE or current_grid[x] == BURNING_FIRE:
                    counter_fire_in_neighborhood += 1

            if current_grid[row, col] == STREET:
                new_grid[row, col] = STREET
            elif current_grid[row, col] == YOUNG_TREE:
                if random.random() <= ALPHA:
                    new_grid[row, col] = GROWING_TREE
                else:
                    new_grid[row, col] = YOUNG_TREE
            elif current_grid[row, col] == GROWING_TREE:
                if random.random() <= ALPHA:
                    new_grid[row, col] = TREE
                elif counter_fire_in_neighborhood > 0 and random.random() <= BETA:
                    new_grid[row, col] = NEW_FIRE
                elif random.random() <= DELTA:
                    new_grid[row, col] = NEW_FIRE
                else:
                    new_grid[row, col] = GROWING_TREE
            elif current_grid[row, col] == TREE:
                if counter_fire_in_neighborhood > 0 and random.random() <= BETA:
                    new_grid[row, col] = NEW_FIRE
                elif random.random() <= DELTA:
                    new_grid[row, col] = NEW_FIRE
                else:
                    new_grid[row, col] = TREE
            elif current_grid[row, col] == WEAK_FIRE:
                new_grid[row, col] = YOUNG_TREE
            elif current_grid[row, col] == BURNING_FIRE:
                new_grid[row, col] = WEAK_FIRE
            elif new_grid[row, col] == NEW_FIRE:
                new_grid[row, col] = BURNING_FIRE

        self.current_state_grid = new_grid
        self.steps += 1


ca = ExtendedForestFireCA()
ca.run(WINDOW_WIDTH, WINDOW_HEIGHT, BLOCK_SIZE, REFRESH_TIME)
