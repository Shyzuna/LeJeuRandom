# -*-coding:UTF-8 -*

from units.BaseUnit import BaseUnit

import os, pygame
GAME_PATH  = os.path.dirname(os.path.realpath(__file__)) + '/../..'

AXIS_X = 0
AXIS_Y = 1

class Player(BaseUnit):

    def __init__(self, playerData=None, *containers):
        BaseUnit.__init__(self, *containers)
        if playerData is None:
            self.image = pygame.image.load(GAME_PATH+'/resources/tiles/player.bmp').convert()
            self.rect = self.image.get_rect()
            self.speed = 3
            self.x = 100
            self.y = 100
            self.rect.top = 100
            self.rect.left = 100
        else:
            pass

    def move(self, direction, axis):
        displacement = direction* self.speed
        if axis == AXIS_X:
            self.rect.move_ip(direction * self.speed, 0)
        elif axis == AXIS_Y:
            self.rect.move_ip(0, direction * self.speed)
        self.rect = self.rect.clamp(pygame.Rect(0, 0, 800, 600))
