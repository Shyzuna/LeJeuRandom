# -*-coding:UTF-8 -*
#Manage the maps

import os, pygame
from manager.Singleton import Singleton

@Singleton
class MapManager:

    def __init__(self):
        self._sizeScreen = (800,600)
        # _tileSize = (width, height)
        self._tileSize = (32,32)
        self._currentMapPath = ""
        self._currentMapName = ""
        self._mapLoaded = False
        self._mapW = 0
        self._mapH = 0
        self._currentMap = []
        self._tileList = []

    def loadMap(self, path):
        self._mapLoaded = False
        self._currentMapPath = path
        with open(self._currentMapPath, "r") as file:
            i = 0
            for line in file:
                if i == 0:
                    self._currentMapName = line
                elif i == 1:
                    self._mapW = int(line.split("x")[0])
                    self._mapH = int(line.split("x")[1])
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

    def addTile(self, number, name, path):
        tile = (name, pygame.image.load(path))
        self._tileList.insert(number,tile)

    def delTile(self, number):
        del self._tileList[number]

    def blitTiles(self, pos, screen):

        caseX = (pos[0] - self._sizeScreen[0]/2) // self._tileSize[0]
        caseY = (pos[1] - self._sizeScreen[1]/2) // self._tileSize[1]
        restX = (pos[0] - self._sizeScreen[0]/2) % self._tileSize[0]
        restY = (pos[1] - self._sizeScreen[1]/2) % self._tileSize[1]

        #check if we are in border of the map
        if pos[0] - self._sizeScreen[0]/2 < 0:
            caseX = 0
            restX = 0

        if pos[1] - self._sizeScreen[1]/2 < 0:
            caseY = 0
            restY = 0

        if pos[0] + self._sizeScreen[0]/2 > self.mapWidthPixels:
            caseX = (self.mapWidthPixels - self._sizeScreen[0]) // self._tileSize[0]
            restX = (self.mapWidthPixels - self._sizeScreen[0]) % self._tileSize[0]

        if pos[1] + self._sizeScreen[1]/2 > self.mapHeightPixels:
            caseY = (self.mapHeightPixels - self._sizeScreen[1]) // self._tileSize[1]
            restY = (self.mapHeightPixels - self._sizeScreen[1]) % self._tileSize[1]

        startBlitX = 0 - restX
        startBlitY = 0 - restY
        i = int(caseX)
        j = int(caseY)

        #Line
        while startBlitY < self._sizeScreen[1]:
            startBlitX = 0 - restX
            i = int(caseX)
            #Col
            while startBlitX < self._sizeScreen[0]:
                blitPos = (startBlitX, startBlitY)
                screen.blit(self._tileList[self._currentMap[i][j]][1],blitPos)
                startBlitX += self._tileSize[0]
                i += 1
            startBlitY += self._tileSize[1]
            j += 1

    @property
    def mapWidthPixels(self):
        return self._mapW * self._tileSize[0]

    @property
    def mapHeightPixels(self):
        return self._mapH * self._tileSize[1]
