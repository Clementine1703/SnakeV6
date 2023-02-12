import pygame
from settings import active_settings

screen = pygame.display.set_mode(
    (active_settings['arena_size'][0], active_settings['arena_size'][1]))
pygame.display.set_caption('Змеюка')
clock = pygame.time.Clock()
font_score = pygame.font.Font(None, 36)
font_gameover = pygame.font.Font(None, 100)
current_speed = active_settings['speed']
