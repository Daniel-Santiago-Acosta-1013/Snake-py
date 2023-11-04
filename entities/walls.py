import pygame
import random
from entities.constants import SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE

WALL_COLOR = (110, 84, 148)  # Color #6e5494

class Walls:
    def __init__(self, snake, food):
        self.positions = self.generate_walls(snake, food)

    def generate_walls(self, snake, food):
        walls = set()
        while len(walls) < 10:  # Generamos 10 paredes para empezar
            wall = (random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1),
                    random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1))
            if wall not in snake.body and wall != food:
                walls.add(wall)
        return walls

    def draw(self, screen):
        for wall in self.positions:
            pygame.draw.rect(screen, WALL_COLOR, (wall[0] * CELL_SIZE, wall[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def collides_with_walls(self, position):
        return position in self.positions
