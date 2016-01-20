# -*-coding:UTF-8 -*

from units.BaseUnit import BaseUnit
from manager.MapManager import MapManager

import os, pygame
GAME_PATH  = os.path.dirname(os.path.realpath(__file__)) + '/../..'

SCREENRECT = pygame.Rect(0, 0, 800, 600)


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
            # Hitbox = (top, left, down right)
            self.hitbox = (16, 16, 16, 16)
            # Starting position
            self.rect.top = 100 - self.hitbox[0]
            self.rect.left = 100 - self.hitbox[1]
        else:
            pass

    def move(self, direction, axis):
        tileW = MapManager.Instance()._tileSize[0]
        tileH = MapManager.Instance()._tileSize[1]
        # mapsize in pixels: (width, height)
        mapsize = MapManager.Instance()._mapW * tileW, MapManager.Instance()._mapH * tileH

        displacement = direction* self.speed

        if axis == AXIS_X:
            if (self.x - self.hitbox[1]) + displacement > 0 and (self.x + self.hitbox[3]) + displacement < mapsize[0]:
                if self.x < SCREENRECT.width // 2 or mapsize[0] - self.x < SCREENRECT.width // 2:
                    self.rect.move_ip(displacement, 0)
                self.x += displacement
            # Handling map limits
            else:
                # If going to the left: set position to minimum on X axis
                if displacement < 0:
                    self.x = self.hitbox[1]
                # Else going to the right: set position to maximum on X axis
                else:
                    self.x = mapsize[0] - self.hitbox[3]
                self.rect.move_ip(displacement, 0)


        elif axis == AXIS_Y:
            if (self.y - self.hitbox[0]) + displacement > 0 and (self.y + self.hitbox[2]) + displacement < mapsize[1]:
                if self.y < SCREENRECT.height // 2 or mapsize[1] - self.y < SCREENRECT.height // 2:
                    self.rect.move_ip(0, displacement)
                self.y += displacement
            # Handling map limits
            else:
                # If going to the top: set position to minimum on Y axis
                if displacement < 0:
                    self.y = self.hitbox[0]
                # Else going to the bottom: set position to maximum on Y axis
                else:
                    self.y = mapsize[1] - self.hitbox[2]
                self.rect.move_ip(0, displacement)
        self.rect = self.rect.clamp(SCREENRECT)
