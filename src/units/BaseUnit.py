# -*-coding:UTF-8 -*
"""Base Unit"""

import pygame

class BaseUnit(pygame.sprite.Sprite):

    def __init__(self, *containers):
        pygame.sprite.Sprite.__init__(self, *containers)
