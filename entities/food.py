import random
from entities.constants import SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE, GOLDEN_FOOD_COLOR

def get_new_food(snake, walls):
    while True:
        food = (random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1),
                random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1))
        if food not in snake.body and food not in walls.positions:
            return food

def get_golden_food(snake, walls):
    while True:
        golden_food = (random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1),
                       random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1))
        if golden_food not in snake.body and golden_food not in walls.positions:
            return golden_food