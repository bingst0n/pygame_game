import pygame
import os
import config
import functions
import player
import tilemap

# Necessary Init
pygame.init()
running = True
dt = 0
basemovespeed = 4
startpos = pygame.Vector2(6, 4)
xoff = 0
yoff = 0

# Load tilemap layers
layer0 = tilemap.load_tilemap_layer("layer0.csv", "world1")
layer1 = tilemap.load_tilemap_layer("layer1.csv", "world1")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    print(player.player_pos.x, player.player_pos.y)

    config.screen.fill("black")

    keys = pygame.key.get_pressed()

    # Calculate normalizer for diagonal movement
    if abs(keys[pygame.K_DOWN] - keys[pygame.K_UP]) + abs(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) == 2:
        normalizer = 1/(2**(1/2))
    else:
        normalizer = 1

    # Calculate movespeed (sprint with X key)
    if keys[pygame.K_x] == 1:
        movespeed = basemovespeed * (5/3)
    else:
        movespeed = basemovespeed

    # Update player and get current sprite
    player_image = player.update_player(keys, dt, movespeed, normalizer, layer0)
    
    # Calculate camera offset
    xoff = player.player_pos.x - startpos.x
    yoff = player.player_pos.y - startpos.y

    # Render layers with player in between
    
    tilemap.drawlayer(layer0, -xoff, -yoff)
    tilemap.drawlayer(layer1, -xoff, -yoff)
    functions.drawatpos(startpos.x, startpos.y, player_image)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = config.clock.tick(60) / 1000

pygame.quit()