# -*-coding:UTF-8 -*
"""Default Tile"""

from units.BaseUnit import BaseUnit

class BaseTile(BaseUnit):

    def __init__(self, number=0, name="", path="", solid=False, *containers):
        BaseUnit.__init__(self, *containers)
        self._number = number
        self._name = name
        self._path = path
        self._solid = solid
