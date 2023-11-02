import random
from entities.constants import SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE

def get_new_food(snake):
  while True:
    food = (random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1),
            random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1))
    if food not in snake.body:
      return food
