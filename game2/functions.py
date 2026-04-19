import pygame
import config

def drawatpos(x, y, tile):
    draw_x = round(x * config.tilesize)*config.scale
    draw_y = round(y * config.tilesize)*config.scale
    config.screen.blit(tile, (draw_x, draw_y))