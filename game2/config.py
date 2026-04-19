import pygame
import os


# Necessary Init
base_path = os.path.dirname(__file__)
tilesize = 24
scale = 3
cols = 12
rows = 8
screen = pygame.display.set_mode((tilesize*scale*cols, tilesize*scale*rows), pygame.DOUBLEBUF | pygame.HWSURFACE)
clock = pygame.time.Clock()