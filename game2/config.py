import pygame
import os


# Necessary Init
base_path = os.path.dirname(__file__)
tilesize = 16
scale = 3
cols = 18
rows = 12
screen = pygame.display.set_mode((tilesize*scale*cols, tilesize*scale*rows))
clock = pygame.time.Clock()