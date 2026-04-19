import pygame
import config
import os
import functions
import csv
import math

obstacles = []

# Tile Image Cache
tile_images = {}

def load_tile_image(tile_id):
    if tile_id not in tile_images:
        tile_path = os.path.join(config.base_path, f"assets/tiles/{tile_id}.png")
        tile_img = pygame.image.load(tile_path).convert_alpha()
        scaled_size = config.tilesize * config.scale
        tile_images[tile_id] = pygame.transform.scale(tile_img, (scaled_size, scaled_size))
    return tile_images[tile_id]

# Tilemap Logic
def load_tilemap_layer(layer_name, world):
    tilemap_path = os.path.join(config.base_path, f"assets/tilemap/{world}", layer_name)
    tilemap_data = []
    
    with open(tilemap_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            curr_row = []
            if len(row)>0:
                for tile in row:
                    usabletile = int(tile)
                    curr_row.append(usabletile)
                    if usabletile == 3 or usabletile == 4:
                        obstacles.append([row, tile])
            tilemap_data.append(curr_row)
    
    return tilemap_data

def is_tile_solid(x, y, layer_data):
    tile_x = math.floor(x)
    tile_y = math.floor(y)
    
    if tile_y < 0 or tile_y >= len(layer_data):
        return True
    elif tile_x < 0 or tile_x >= len(layer_data[tile_y]):
        return True
    else:
        tile_id = layer_data[tile_y][tile_x]
        if tile_id == 3 or tile_id == 4:
            return True
        else:
            return False

def drawlayer(layer_data, xoffset, yoffset):
    for row_id, row in enumerate(layer_data):
        for col_id, tile in enumerate(row):
            if tile != -1:
                x = round((col_id+xoffset) * config.tilesize) * config.scale
                y = round((row_id+yoffset) * config.tilesize) * config.scale
                tile_image = load_tile_image(tile)
                config.screen.blit(tile_image, (x, y))

print(obstacles)