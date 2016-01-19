# -*-coding:UTF-8 -*
"""Manage the maps"""

import os
from manager.Singleton import Singleton

@Singleton
class MapManager:

    def __init__(self):
        self._currentMapPath = ""
        self._currentMapName = ""
        self._mapLoaded = False
        self._mapW = 0
        self._mapH = 0
        self._currentMap = []

    def loadMap(self, path):
        self._mapLoaded = False
        self._currentMapPath = path
        with open(self._currentMapPath, "r") as file:
            i = 0
            for line in file:
                if i == 0:
                    self._currentMapName = line
                elif i == 1:
                    self._mapW = line.split("x")[0]
                    self._mapH = line.split("x")[1]
                elif i == 2:
                    pass
                else:
                    lineMap = []
                    for c in line:
                        if c != "\n":
                            lineMap.append(int(c))
                    self._currentMap.append(lineMap)
                i += 1
        self._mapLoaded = True

    def printMap(self):
        if self._mapLoaded:
            for line in self._currentMap:
                chaine = ""
                for val in line:
                    chaine += str(val)
                print(chaine)
