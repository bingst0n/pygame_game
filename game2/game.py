import pygame
import os
import config
import functions

# Necessary Init
pygame.init()
running = True
dt = 0
basemovespeed=4

# Player Movement and Logic
player_pos = pygame.Vector2(5,5)

# Setup Sprites
playersprites = []
playerleft = pygame.image.load(os.path.join(config.base_path, "assets/characters/player/playerleft.png")).convert_alpha()
playerdown = pygame.image.load(os.path.join(config.base_path, "assets/characters/player/playerdown.png")).convert_alpha()
playerup = pygame.image.load(os.path.join(config.base_path, "assets/characters/player/playerup.png")).convert_alpha()
playerright = pygame.image.load(os.path.join(config.base_path, "assets/characters/player/playerright.png")).convert_alpha()
playersprites.append(pygame.transform.scale(playerleft, (config.tilesize * config.scale, config.tilesize * config.scale)))
playersprites.append(pygame.transform.scale(playerdown, (config.tilesize * config.scale, config.tilesize * config.scale)))
playersprites.append(pygame.transform.scale(playerup, (config.tilesize * config.scale, config.tilesize * config.scale)))
playersprites.append(pygame.transform.scale(playerright, (config.tilesize * config.scale, config.tilesize * config.scale)))

player_image = playersprites[1]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    config.screen.fill("black")
    
    functions.drawatpos(player_pos.x, player_pos.y, player_image)

    keys = pygame.key.get_pressed()

    if abs(keys[pygame.K_DOWN] - keys[pygame.K_UP]) + abs(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) == 2:
        normalizer = 1/(2**(1/2))
    else:
        normalizer = 1

    if keys[pygame.K_x] == 1:
        movespeed = basemovespeed * (5/3)
    else:
        movespeed = basemovespeed

    if abs(keys[pygame.K_DOWN]) + abs(keys[pygame.K_UP]) + abs(keys[pygame.K_RIGHT]) + abs(keys[pygame.K_LEFT]) > 0:
        moving = True
    
    xvel = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * normalizer
    yvel = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * normalizer

    # Handle Sprite Updates
    if keys[pygame.K_RIGHT] == 1:
        dir = 3
        player_image = playersprites[dir]
    elif keys[pygame.K_LEFT] == 1:
        dir = 0
        player_image = playersprites[dir]
    elif keys[pygame.K_DOWN] == 1:
        dir = 1
        player_image = playersprites[dir]
    elif keys[pygame.K_UP] == 1:
        dir = 2
        player_image = playersprites[dir]

    player_pos.x += xvel * movespeed * dt
    player_pos.y += yvel * movespeed * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = config.clock.tick(60) / 1000

pygame.quit()