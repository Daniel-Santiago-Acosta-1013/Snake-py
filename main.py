import pygame
from entities.constants import SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE, BACKGROUND_COLOR, SNAKE_COLOR, FOOD_COLOR, UP, DOWN, LEFT, RIGHT, GOLDEN_FOOD_COLOR
from entities.snake import Snake
from entities.walls import Walls
from entities.food import get_new_food, get_golden_food
from entities.ui_manager import display_game_over, display_paused, display_score

# Configuración inicial de pygame
pygame.init()
CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")

def main():
    snake = Snake()
    walls = Walls(snake, None)
    food = get_new_food(snake, walls)
    golden_food = None
    golden_food_available = False
    paused = False
    score = 0
    max_score = 0
    normal_food_eaten = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
                    if paused:
                        display_paused(SCREEN)
                elif not paused:
                    if event.key in [pygame.K_w, pygame.K_UP] and snake.direction != DOWN:
                        snake.change_direction(UP)
                    elif event.key in [pygame.K_s, pygame.K_DOWN] and snake.direction != UP:
                        snake.change_direction(DOWN)
                    elif event.key in [pygame.K_a, pygame.K_LEFT] and snake.direction != RIGHT:
                        snake.change_direction(LEFT)
                    elif event.key in [pygame.K_d, pygame.K_RIGHT] and snake.direction != LEFT:
                        snake.change_direction(RIGHT)
        
        if paused:
            continue

        snake.move()

        if snake.body[0] == food:
            snake.grow()
            normal_food_eaten += 1
            if normal_food_eaten % 5 == 0:  # Cada 5 comidas normales, aparece una comida dorada
                golden_food = get_golden_food(snake, walls)
                golden_food_available = True
            food = get_new_food(snake, walls)
            score += 1
            max_score = max(score, max_score)

        if snake.collides_with_itself() or snake.body[0] in walls.positions:
            display_game_over(SCREEN)
            pygame.time.wait(2000)
            snake = Snake()
            walls = Walls(snake, None)
            food = get_new_food(snake, walls)
            normal_food_eaten = 0  # Reseteamos el contador de comidas normales
            golden_food_available = False
            score = 0

        if golden_food_available:
            pygame.draw.rect(SCREEN, GOLDEN_FOOD_COLOR, (golden_food[0] * CELL_SIZE, golden_food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        if golden_food_available and snake.body[0] == golden_food:
            snake.shrink()
            golden_food_available = False  # La comida dorada desaparece después de ser comida
            golden_food = None  # Reiniciar la comida dorada

        SCREEN.fill(BACKGROUND_COLOR)
        for segment in snake.body:
            pygame.draw.rect(SCREEN, SNAKE_COLOR, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(SCREEN, FOOD_COLOR, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        walls.draw(SCREEN)

        display_score(SCREEN, score, max_score)

        pygame.display.flip()
        CLOCK.tick(10)

if __name__ == "__main__":
    main()
