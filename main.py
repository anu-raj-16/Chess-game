import pygame

pygame.init()
WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.SysFont('fonts/8-bit Arcade Out.ttf', 20)
big_font = pygame.font.SysFont('fonts/8-bit Arcade Out.ttf', 50)
timer = pygame.time.Clock()
fps = 60