import random

import numpy as np
from CellularAutomataBlock2D import CellularAutomataBlock2D as CA

POPULATION_1 = 1
POPULATION_2 = 2
POPULATION_3 = 3
POPULATION_4 = 4
POPULATION_5 = 5
EMPTY = 0

MOVEMENT_RATE = 1 / 7
MIGRATION_RATE = 1 / 7
INVASION_RATE = 5 / 7

WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
BLOCK_SIZE = 5
REFRESH_TIME = 0

NUMBER_OF_INITIAL_POPS_PER_POP = 100

BLACK = (0, 0, 0)
GREY = (12, 211, 211)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
BROWN = (13, 248, 220)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class PopulationDynamics(CA):

    def __init__(self):
        name = "Populations at total war CA"
        neighborhood = 1
        states_and_colors = [(EMPTY, BLACK), (POPULATION_1, RED), (POPULATION_2, YELLOW), (POPULATION_3, GREEN), (POPULATION_4, ORANGE), (POPULATION_5, BLUE)]
        initial_state_grid = self.generate_initial_state_grid()
        super().__init__(name, neighborhood, states_and_colors, initial_state_grid)

    def generate_initial_state_grid(self):
        grid = np.zeros((WINDOW_HEIGHT // BLOCK_SIZE, WINDOW_WIDTH // BLOCK_SIZE))

        for i in range(6):
            if i == 0:
                continue
            for x in range(NUMBER_OF_INITIAL_POPS_PER_POP):
                random_col = np.random.randint(0, WINDOW_WIDTH // BLOCK_SIZE)
                random_row = np.random.randint(0, WINDOW_HEIGHT // BLOCK_SIZE)
                grid[random_row, random_col] = i

        return grid

    def update(self):
        current_grid = self.current_state_grid
        new_grid = np.zeros((current_grid.shape[0], current_grid.shape[1]))

        for row, col in np.ndindex(current_grid.shape):
            neighborhood = self.get_neighborhood(row, col)

            neighbor = random.choice(neighborhood)
            decision_list = [0, 1, 2]
            decision = random.choices(decision_list, weights=(INVASION_RATE, MIGRATION_RATE, MOVEMENT_RATE), k=1)[0]

            if decision == 0:
                if current_grid[row, col] == POPULATION_1 and current_grid[neighbor[0], neighbor[1]] == EMPTY:
                    new_grid[neighbor[0], neighbor[1]] = POPULATION_1
                elif current_grid[row, col] == EMPTY and current_grid[neighbor[0], neighbor[1]] == POPULATION_1:
                    new_grid[row, col] = POPULATION_1
                elif current_grid[row, col] == POPULATION_2 and current_grid[neighbor[0], neighbor[1]] == EMPTY:
                    new_grid[neighbor[0], neighbor[1]] = POPULATION_2
                elif current_grid[row, col] == EMPTY and current_grid[neighbor[0], neighbor[1]] == POPULATION_2:
                    new_grid[row, col] = POPULATION_2
                elif current_grid[row, col] == POPULATION_3 and current_grid[neighbor[0], neighbor[1]] == EMPTY:
                    new_grid[neighbor[0], neighbor[1]] = POPULATION_3
                elif current_grid[row, col] == EMPTY and current_grid[neighbor[0], neighbor[1]] == POPULATION_3:
                    new_grid[row, col] = POPULATION_3
                elif current_grid[row, col] == POPULATION_4 and current_grid[neighbor[0], neighbor[1]] == EMPTY:
                    new_grid[neighbor[0], neighbor[1]] = POPULATION_4
                elif current_grid[row, col] == EMPTY and current_grid[neighbor[0], neighbor[1]] == POPULATION_4:
                    new_grid[row, col] = POPULATION_4
                elif current_grid[row, col] == POPULATION_5 and current_grid[neighbor[0], neighbor[1]] == EMPTY:
                    new_grid[neighbor[0], neighbor[1]] = POPULATION_5
                elif current_grid[row, col] == EMPTY and current_grid[neighbor[0], neighbor[1]] == POPULATION_5:
                    new_grid[row, col] = POPULATION_5
                else:
                    new_grid[row, col] = current_grid[row, col]
            if decision == 1:
                if current_grid[row, col] == EMPTY or current_grid[neighbor[0], neighbor[1]] == EMPTY:
                    new_grid[row, col] = current_grid[row, col]
                else:
                    new_grid[row, col] = current_grid[row, col]
                    new_grid[neighbor[0], neighbor[1]] = current_grid[row, col]
            if decision == 2:
                new_grid[row, col] = current_grid[neighbor[0], neighbor[1]]
                new_grid[neighbor[0], neighbor[1]] = current_grid[row, col]

        self.current_state_grid = new_grid
        self.steps += 1


ca = PopulationDynamics()
ca.run(WINDOW_WIDTH, WINDOW_HEIGHT, BLOCK_SIZE, REFRESH_TIME)
