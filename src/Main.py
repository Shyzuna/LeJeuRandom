# -*-coding:UTF-8 -*
"""Main"""

import sys, pygame, os
from manager.MapManager import MapManager
pygame.init()

size = width, height = 800, 600

screen = pygame.display.set_mode(size)
defaultColor = 0,0,0
MapManager.Instance().loadMap("../resources/maps/map1.map")
MapManager.Instance().printMap()

"""Event loop"""
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(defaultColor)
    pygame.display.flip()
