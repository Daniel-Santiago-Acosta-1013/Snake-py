
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE, WHITE, GREEN, RED, UP, DOWN, LEFT, RIGHT
from entities.snake import Snake
from entities.food import get_new_food

# Configuración inicial de pygame
pygame.init()
CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")

def main():
  snake = Snake()
  food = get_new_food(snake)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        return

      if event.type == pygame.KEYDOWN:
        if event.key in [pygame.K_w, pygame.K_UP] and snake.direction != DOWN:
          snake.change_direction(UP)
        elif event.key in [pygame.K_s, pygame.K_DOWN
                           ] and snake.direction != UP:
          snake.change_direction(DOWN)
        elif event.key in [pygame.K_a, pygame.K_LEFT
                           ] and snake.direction != RIGHT:
          snake.change_direction(LEFT)
        elif event.key in [pygame.K_d, pygame.K_RIGHT
                           ] and snake.direction != LEFT:
          snake.change_direction(RIGHT)

    snake.move()

    if snake.body[0] == food:
      snake.grow()
      food = get_new_food(snake)

    if snake.collides_with_itself():
      snake = Snake()
      food = get_new_food(snake)

    SCREEN.fill(WHITE)
    for segment in snake.body:
      pygame.draw.rect(SCREEN, GREEN,
                       (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE,
                        CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(
        SCREEN, RED,
        (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()
    CLOCK.tick(10)


if __name__ == "__main__":
    main()