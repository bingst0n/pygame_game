import pygame
import os


# Necessary Init
base_path = os.path.dirname(__file__)
tilesize = 32
scale = 4
cols = 9
rows = 6
screen = pygame.display.set_mode((tilesize*scale*cols, tilesize*scale*rows))
clock = pygame.time.Clock()