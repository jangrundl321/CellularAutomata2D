import sys
import pygame

class CellularAutomataBlock2D:

    def __init__(self, name, neighborhood, states_and_colors, initial_state_grid):
        self.name = name
        self.neighborhood = neighborhood
        self.steps = 0
        self.torus = False  # not implemented
        self.states_and_colors = states_and_colors
        self.initial_state_grid = initial_state_grid
        self.current_state_grid = initial_state_grid

    def get_neighborhood(self, row, col, ):
        neighborhood = []
        grid = self.current_state_grid

        # moore neighborhood:
        if self.neighborhood == 0:
            for x, y in ((row + 1, col - 1), (row + 1, col + 1),
                         (row - 1, col), (row + 1, col), (row, col - 1),
                         (row, col + 1), (row - 1, col - 1), (row - 1, col + 1)):
                if not (0 <= x < len(grid) and 0 <= y < len(grid[x])):
                    continue
                else:
                    neighborhood.append((x, y))
        # neumann
        else:
            for x, y in (
                    (row - 1, col), (row + 1, col), (row, col - 1),
                    (row, col + 1)):
                if not (0 <= x < len(grid) and 0 <= y < len(grid[x])):
                    # out of bounds
                    continue
                else:
                    neighborhood.append((x, y))
        return neighborhood

    def update(self):
        pass

    def draw(self, window_width, window_height, block_size, screen):
        grid_used_for_drawing = self.current_state_grid

        for x_window in range(0, window_width, block_size):
            for y_window in range(0, window_height, block_size):
                rect = pygame.Rect(x_window, y_window, block_size, block_size)
                x_grid = x_window // block_size
                y_grid = y_window // block_size

                for sc in self.states_and_colors:
                    state = sc[0]
                    color = sc[1]

                    if grid_used_for_drawing[x_grid, y_grid] == state:
                        pygame.draw.rect(screen, color, rect, 0)

    def run(self, window_width, window_height, block_size, refresh_time):
        BLACK = (0, 0, 0)
        pygame.init()
        SCREEN = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption(self.name)
        CLOCK = pygame.time.Clock

        while True:
            SCREEN.fill(BLACK)
            pygame.time.wait(refresh_time)
            self.draw(window_width, window_height, block_size, SCREEN)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            self.update()
            SCREEN.fill(BLACK)
