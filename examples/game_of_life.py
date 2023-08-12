import numpy as np
from CellularAutomataBlock2D import CellularAutomataBlock2D as CA

DEAD = 0
ALIVE = 1

WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
BLOCK_SIZE = 5
REFRESH_TIME = 10

NUMBER_OF_ALIVE_CELLS = 5000

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)


class GameOfLifeCA(CA):

    def __init__(self):
        name = "Game of Life CA"
        neighborhood = 0
        states_and_colors = [(ALIVE, BLACK), (DEAD, WHITE)]
        initial_state_grid = self.generate_initial_state_grid()
        super().__init__(name, neighborhood, states_and_colors, initial_state_grid)

    def generate_initial_state_grid(self):
        grid = np.zeros((WINDOW_WIDTH // BLOCK_SIZE, WINDOW_HEIGHT // BLOCK_SIZE))

        for i in range(NUMBER_OF_ALIVE_CELLS):
            random_col = np.random.randint(0, WINDOW_WIDTH // BLOCK_SIZE)
            random_row = np.random.randint(0, WINDOW_HEIGHT // BLOCK_SIZE)

            if grid[random_row, random_col] == DEAD:
                grid[random_row, random_col] = ALIVE

        return grid

    def update(self):
        current_grid = self.current_state_grid
        new_grid = np.zeros((current_grid.shape[0], current_grid.shape[1]))

        for row, col in np.ndindex(current_grid.shape):
            neighborhood = self.get_neighborhood(row, col)
            counter_alive_cells_in_neighborhood = 0

            for x in neighborhood:
                if current_grid[x] == ALIVE:
                    counter_alive_cells_in_neighborhood += 1

            if current_grid[row, col] == ALIVE and (
                    counter_alive_cells_in_neighborhood == 2 or counter_alive_cells_in_neighborhood == 3):
                new_grid[row, col] = ALIVE
            elif current_grid[row, col] == ALIVE and counter_alive_cells_in_neighborhood <= 2:
                new_grid[row, col] = DEAD
            elif current_grid[row, col] == ALIVE and counter_alive_cells_in_neighborhood > 3:
                new_grid[row, col] = DEAD
            elif current_grid[row, col] == DEAD and counter_alive_cells_in_neighborhood == 3:
                new_grid[row, col] = ALIVE
            else:
                new_grid[row, col] = DEAD

        self.current_state_grid = new_grid
        self.steps += 1


ca = GameOfLifeCA()
ca.run(WINDOW_WIDTH, WINDOW_HEIGHT, BLOCK_SIZE, REFRESH_TIME)
