# -*-coding:UTF-8 -*
"""Main"""

import sys, pygame
from manager.MapManager import MapManager
pygame.init()

size = width, height = 800, 600

screen = pygame.display.set_mode(size)
defaultColor = 0,0,0
MapManager.Instance().loadMap("../resources/maps/map1.map")
MapManager.Instance().printMap()
MapManager.Instance().addTile(0, "grass", "../resources/tiles/grass.bmp")
MapManager.Instance().addTile(1, "rock", "../resources/tiles/rock.bmp")
MapManager.Instance().addTile(10, "player", "../resources/tiles/player.bmp")

pos = (100,100)

"""Event loop"""
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(defaultColor)
    MapManager.Instance().blitTiles(pos, screen)
    pygame.display.flip()
