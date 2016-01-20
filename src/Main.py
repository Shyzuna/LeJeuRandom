# -*-coding:UTF-8 -*
"""Main"""

import sys, os, pygame
from manager.MapManager import MapManager
from units.Player import Player
SRC_DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def convertToViewport(position, screen):
    x = position[0]
    y = position[1]
    if(position[0] > screen[0]/2):
        x = screen[0]/2
    if(position[1] > screen[1]/2):
        y = screen[1]/2
    return (x,y)

pygame.init()

clock = pygame.time.Clock()

size = width, height = 800, 600

screen = pygame.display.set_mode(size)
defaultColor = 0,0,0
MapManager.Instance().loadMap(SRC_DIR_PATH + "/../resources/maps/map1.map")
MapManager.Instance().printMap()
MapManager.Instance().addTile(0, "grass", SRC_DIR_PATH + "/../resources/tiles/grass.bmp")
MapManager.Instance().addTile(1, "rock", SRC_DIR_PATH + "/../resources/tiles/rock.bmp")
MapManager.Instance().addTile(10, "player", SRC_DIR_PATH + "/../resources/tiles/player.bmp")


player = Player()
allgrp = pygame.sprite.RenderUpdates()
player.add(allgrp)

bg = pygame.Surface(size)

"""Event loop"""
pygame.key.set_repeat(1,10)
while 1:

    allgrp.clear(screen, bg)
    allgrp.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move(-1, 1)
            if event.key == pygame.K_DOWN:
                player.move(1, 1)
            if event.key == pygame.K_RIGHT:
                player.move(1, 0)
            if event.key == pygame.K_LEFT:
                player.move(-1, 0)


    pos = (player.rect.left,player.rect.top)
    pos2 = convertToViewport(pos,size)
    screen.fill(defaultColor)
    MapManager.Instance().blitTiles(pos, screen)
    pygame.display.flip()

    # Draw the sprites of group "allgrp" on the screen
    dirty = allgrp.draw(screen)
    # Update the display
    pygame.display.update(dirty)

    # Frequency (FPS) limit
    clock.tick(30)
