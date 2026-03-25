import pygame
import config
import tilemap
import player

running = True
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    tilemap.draw_below_player()
    player.update(dt)
    player.draw()
    #tilemap.draw_above_player()

    pygame.display.flip()

    dt = config.clock.tick(60) / 1000

pygame.quit()
