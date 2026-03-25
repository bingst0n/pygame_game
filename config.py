import pygame

pygame.init()

tilesize = 16
rows = 18
cols = 32
scaling = 2

screen = pygame.display.set_mode((cols * scaling * tilesize, rows * scaling * tilesize))
clock = pygame.time.Clock()
