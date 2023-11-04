import pygame
from entities.constants import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, SCORE_FONT_SIZE, SCORE_POS

def get_font():
    return pygame.font.SysFont('arial', 36)

def get_game_over_text():
    font = get_font()
    return font.render('¡Has perdido!', True, (0, 0, 0))

def get_paused_text():
    font = get_font()
    return font.render('Juego en pausa', True, (0, 0, 0))

def display_modal(screen, text_surface):
    pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 3, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
    screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, SCREEN_HEIGHT // 2 - text_surface.get_height() // 2))
    pygame.display.flip()

def display_game_over(screen):
    display_modal(screen, get_game_over_text())

def display_paused(screen):
    display_modal(screen, get_paused_text())

def get_score_font():
    return pygame.font.SysFont('arial', SCORE_FONT_SIZE)

def display_score(screen, score, max_score):
    font = get_score_font()
    score_text = font.render(f"Score: {score}   Record: {max_score}", True, (0, 0, 0))
    screen.blit(score_text, SCORE_POS)
