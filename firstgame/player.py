import pygame
import os
import config
import tilemap

base_path = os.path.dirname(__file__)

player_sheet = pygame.image.load(os.path.join(base_path, "assets/player.png")).convert_alpha()
playersprites = []
for i in range(4):
    sprite = player_sheet.subsurface(i * config.tilesize, 0, config.tilesize, config.tilesize)
    playersprites.append(pygame.transform.scale(sprite, (config.tilesize * config.scaling, config.tilesize * config.scaling)))
player_image = playersprites[2]

player_pos = pygame.Vector2(26, 16)
move_cooldown = 0.15
xvel = 0
yvel = 0
tiles_remaining = 0

def request_move(x=0, y=0):
    tx = player_pos.x + x
    ty = player_pos.y + y
    if (int(player_pos.x), int(player_pos.y), x, y) not in tilemap.blocked_moves:
        if -1 < tx < config.cols and -1 < ty < config.rows:
            if tilemap.get_layer1_index(tx, ty) not in tilemap.tiletypes["obstacle"] and tilemap.get_layer2_index(tx, ty) not in tilemap.tiletypes["obstacle"]:
                move(x, y)

def move(x, y):
    global xvel, yvel, tiles_remaining
    xvel = x
    yvel = y
    tiles_remaining = 1

def update(dt):
    global tiles_remaining, move_cooldown, player_image
    keys = pygame.key.get_pressed()
    if tiles_remaining > 0:
        step = dt / move_cooldown
        if step >= tiles_remaining:
            player_pos.x = round(player_pos.x)
            player_pos.y = round(player_pos.y)
            tiles_remaining = 0
        else:
            player_pos.x += xvel * step
            player_pos.y += yvel * step
            tiles_remaining -= step
    else:
        if keys[pygame.K_RIGHT] == 1:
            player_image = playersprites[3]
            request_move(1, 0)
        elif keys[pygame.K_LEFT] == 1:
            player_image = playersprites[0]
            request_move(-1, 0)
        elif keys[pygame.K_DOWN] == 1:
            player_image = playersprites[1]
            request_move(0, 1)
        elif keys[pygame.K_UP] == 1:
            player_image = playersprites[2]
            request_move(0, -1)

    if keys[pygame.K_x] == 1:
        move_cooldown = 0.125
    else:
        move_cooldown = 0.2

def draw():
    tilemap.drawatpos(player_pos.x, player_pos.y, player_image)