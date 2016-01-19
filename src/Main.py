# -*-coding:UTF-8 -*
"""Main"""

import sys, pygame
from manager.MapManager import MapManager


def convertToViewport(position, screen):
    x = position[0]
    y = position[1]
    if(position[0] > screen[0]/2):
        x = screen[0]/2
    if(position[1] > screen[1]/2):
        y = screen[1]/2
    return (x,y)

pygame.init()

size = width, height = 800, 600

screen = pygame.display.set_mode(size)
defaultColor = 0,0,0
MapManager.Instance().loadMap("../resources/maps/map1.map")
MapManager.Instance().printMap()
MapManager.Instance().addTile(0, "grass", "../resources/tiles/grass.bmp")
MapManager.Instance().addTile(1, "rock", "../resources/tiles/rock.bmp")
MapManager.Instance().addTile(10, "player", "../resources/tiles/player.bmp")

x = 100
y = 100
"""Event loop"""
pygame.key.set_repeat(1,10)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y -= 1
            if event.key == pygame.K_DOWN:
                y += 1
            if event.key == pygame.K_RIGHT:
                x += 1
            if event.key == pygame.K_LEFT:
                x -= 1

    pos = (x,y)
    pos2 = convertToViewport(pos,size)
    screen.fill(defaultColor)
    MapManager.Instance().blitTiles(pos, screen)
    screen.blit(MapManager.Instance()._tileList[2][1],pos2)
    pygame.display.flip()
