# -*-coding:UTF-8 -*
"""Main"""

import sys, pygame
pygame.init()

size = width, height = 800, 600

screen = pygame.display.set_mode(size)
defaultColor = 0,0,0

"""Event loop"""
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(defaultColor)
    pygame.display.flip()