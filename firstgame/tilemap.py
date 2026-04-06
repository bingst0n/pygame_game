import pygame
import csv
import os
import config

base_path = os.path.dirname(__file__)

spritesheet = pygame.image.load(os.path.join(base_path, "assets/island/tiles.png")).convert_alpha()
tiles_per_row = spritesheet.get_width() // config.tilesize

tile_cache = {}

def get_tile(index):
    if index not in tile_cache:
        col = index % tiles_per_row
        row = index // tiles_per_row
        tile = spritesheet.subsurface(col * config.tilesize, row * config.tilesize, config.tilesize, config.tilesize)
        tile_cache[index] = pygame.transform.scale(tile, (config.tilesize * config.scaling, config.tilesize * config.scaling))
    return tile_cache[index]

tiletypes = {
    "obstacle": [0,1,2,5,8]
}

blocked_moves = {
}

def load_layer(path):
    result = []
    map_reader = csv.reader(open(path))
    for row in map_reader:
        if len(row) > 0:
            new_row = []
            for cell in row:
                new_row.append(int(cell))
            result.append(new_row)
    open(path).close()
    return result

layer1 = load_layer(os.path.join(base_path, "assets/island/maplayer1.csv"))
layer2 = load_layer(os.path.join(base_path, "assets/island/maplayer2.csv"))
#layer3 = load_layer("assets/island/maplayer3.csv")

def get_layer1_index(x, y):
    return layer1[int(y)][int(x)]

def get_layer2_index(x, y):
    return layer2[int(y)][int(x)]
    
#def get_layer3_index(x, y):
#    return layer3[int(y)][int(x)]

def drawatpos(x, y, tile):
    draw_x = x * config.tilesize * config.scaling
    draw_y = y * config.tilesize * config.scaling
    config.screen.blit(tile, (draw_x, draw_y))

def draw_below_player():
    for row_idx in range(len(layer1)):
        row = layer1[row_idx]
        for col_idx in range(len(row)):
            tile_id = row[col_idx]
            if tile_id != -1:
                drawatpos(col_idx, row_idx, get_tile(tile_id))
    for row_idx in range(len(layer2)):
        row = layer2[row_idx]
        for col_idx in range(len(row)):
            tile_id = row[col_idx]
            if tile_id != -1:
                drawatpos(col_idx, row_idx, get_tile(tile_id))
'''
def draw_above_player():
    for row_idx in range(len(layer3)):
        row = layer3[row_idx]
        for col_idx in range(len(row)):
            tile_id = row[col_idx]
            if tile_id != -1:
                drawatpos(col_idx, row_idx, get_tile(tile_id))
'''