import pygame
import config

def drawatpos(x, y, tile):
    draw_x = x * config.tilesize * config.scale
    draw_y = y * config.tilesize * config.scale
    config.screen.blit(tile, (draw_x, draw_y))