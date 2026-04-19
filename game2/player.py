import pygame
import config
import os
import functions
import tilemap

# Player Movement and Logic
xstart=6
ystart=4
player_pos = pygame.Vector2(xstart,ystart)

animationtimer = 0
animspeed = 0.1
currspriteid = 0
direction = 1
playersize = 32 * config.scale

# Setup Sprites
playersprites = []

currplayerarray = []
for i in range(0,4):
    currplayerarray.append(pygame.transform.scale(pygame.image.load(os.path.join(config.base_path, f"assets/characters/player/playerleft/playerleft{i}.png")).convert_alpha(), (playersize, playersize)))
playersprites.append(currplayerarray)
currplayerarray = []
for i in range(0,4):
    currplayerarray.append(pygame.transform.scale(pygame.image.load(os.path.join(config.base_path, f"assets/characters/player/playerdown/playerdown{i}.png")).convert_alpha(), (playersize, playersize)))
playersprites.append(currplayerarray)
currplayerarray = []
for i in range(0,4):
    currplayerarray.append(pygame.transform.scale(pygame.image.load(os.path.join(config.base_path, f"assets/characters/player/playerup/playerup{i}.png")).convert_alpha(), (playersize, playersize)))
playersprites.append(currplayerarray)
currplayerarray = []
for i in range(0,4):
    currplayerarray.append(pygame.transform.scale(pygame.image.load(os.path.join(config.base_path, f"assets/characters/player/playerright/playerright{i}.png")).convert_alpha(), (playersize, playersize)))
playersprites.append(currplayerarray)

def update_player(keys, dt, movespeed, normalizer, collision_layer):
    global animationtimer, currspriteid, direction, player_pos
    
    # Check if moving
    if abs(keys[pygame.K_DOWN]) + abs(keys[pygame.K_UP]) + abs(keys[pygame.K_RIGHT]) + abs(keys[pygame.K_LEFT]) > 0:
        moving = True
    else:
        moving = False
    
    # Update animation
    if moving:
        animationtimer += dt
        if animationtimer >= animspeed:
            animationtimer = 0
            if currspriteid == 3:
                currspriteid = 0
            else:
                currspriteid += 1
    else:
        currspriteid = 0
    
    # Update direction
    if keys[pygame.K_RIGHT] == 1:
        direction = 3
    elif keys[pygame.K_LEFT] == 1:
        direction = 0
    elif keys[pygame.K_DOWN] == 1:
        direction = 1
    elif keys[pygame.K_UP] == 1:
        direction = 2
    
    # Calculate velocity
    xvel = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * normalizer
    yvel = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * normalizer
    
    # Calculate next position
    next_x = player_pos.x + xvel * movespeed * dt
    next_y = player_pos.y + yvel * movespeed * dt
    
    # Player hitbox size in tile units (subtract epsilon so exact boundary doesn't count)
    hitbox = playersize / (config.tilesize * config.scale)
    edge = hitbox
    
    # Check all 4 corners against obstacles
    def blocked(x, y):
        return (tilemap.is_tile_solid(x + 0.3, y + 1, collision_layer) or
                tilemap.is_tile_solid(x + edge - 0.3, y + 1, collision_layer) or
                tilemap.is_tile_solid(x + 0.3, y + edge, collision_layer) or
                tilemap.is_tile_solid(x + edge - 0.3, y + edge, collision_layer))
    
    # Check collision and update position
    if not blocked(next_x, player_pos.y):
        player_pos.x = next_x
    if not blocked(player_pos.x, next_y):
        player_pos.y = next_y
    
    # Return current sprite
    return playersprites[direction][currspriteid]