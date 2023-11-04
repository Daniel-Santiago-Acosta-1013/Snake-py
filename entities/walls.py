import pygame
import random
from entities.constants import SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE

WALL_COLOR = (110, 84, 148)  # Color #6e5494

class Walls:
    def __init__(self, snake, food):
        self.positions = self.generate_walls(snake, food)

    def generate_wall_segment(self, start, direction, length):
        return [(start[0] + i * direction[0], start[1] + i * direction[1]) for i in range(length)]

    def generate_walls(self, snake, food):
        walls = set()
        while len(walls) < 50:  # Intentaremos generar un total de 50 segmentos de pared
            start = (random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1),
                     random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1))
            length = random.randint(2, 5)  # Longitud aleatoria para el segmento de pared
            if random.choice([True, False]):
                direction = (1, 0)  # Horizontal
            else:
                direction = (0, 1)  # Vertical
            
            segment = self.generate_wall_segment(start, direction, length)
            
            # Comprobamos que el segmento no colisione con la comida ni con la serpiente
            if all(pos not in snake.body and pos != food for pos in segment):
                walls.update(segment)
        
        return walls

    def draw(self, screen):
        for wall in self.positions:
            pygame.draw.rect(screen, WALL_COLOR, (wall[0] * CELL_SIZE, wall[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def collides_with_walls(self, position):
        return position in self.positions
