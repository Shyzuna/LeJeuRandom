# -*-coding:UTF-8 -*
"""Default Tile"""

class DefaultTile(pygame.sprite.Sprite):

    def __init__(self, number=0, name="", path="", *groups):
        pygame.sprite.Sprite.__init__(self, *groups)
        self._number = number
        self._name = name
        self._path = path
