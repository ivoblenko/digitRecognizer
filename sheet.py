import pygame as pg


class Sheet:
    def __init__(self):
        self.width = 28
        self.height = 28
        self.blocks = []
        self.clearSheet()
        self.blockWidth = 30
        self.blockHeight = 30
        self.blockBetweenSpace = 5
        self.colorConstant = 255

    def clearSheet(self):
        self.blocks = [[0 for i in range(self.width)] for j in range(self.height)]

    def drawPicture(self, scene, xStartCoord, yStartCoord):
        curXCoord = xStartCoord
        curYCoord = yStartCoord
        for line in self.blocks:
            for pixel in line:
                pg.draw.rect(scene,
                             (self.colorConstant - pixel, self.colorConstant - pixel, self.colorConstant - pixel),
                             (curXCoord, curYCoord, self.blockWidth, self.blockHeight))
                curXCoord += self.blockWidth
            curYCoord += self.blockHeight

    def updateSheet(self, xCoord, yCoord, color, xStartCoord, yStartCoord, scene):
        self.blocks[xCoord // self.blockWidth][yCoord // self.blockHeight] = color
        self.drawPicture(scene, xStartCoord, yStartCoord)
