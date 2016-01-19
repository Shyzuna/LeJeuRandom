# -*-coding:UTF-8 -*
"""Manage the maps"""

from manager.Singleton import Singleton

@Singleton
class MapManager:

    def __init__(self):
        self._currentMapPath = ""
        self._currentMapName = ""
        self._mapLoaded = False
        self._mapW = 0
        self._mapH = 0
        self._currentMap = array()
