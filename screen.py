import pygame as pg


class Screen:
    def __init__(self):
        self.width = 28
        self.height = 28
        self.blocks = []
        self.blockWidth = 30
        self.blockHeight = 30
        self.blockBetweenSpace = 5
        self.colorConstant = 255
        self.bigColorCoef = 155
        self.smallColorCoef = 100
        self.scene = pg.display.set_mode((1280, 840))
        self.xStartCoord = 0
        self.yStartCoord = 0
        pg.font.init()

        self.clearSheet()
        self.drawDigitLable("-")
        self.drawLabel()

    def learningNetwork(self, run=False):
        if run:
            self.drawDigitLable("Обучение")
        else:
            self.drawDigitLable("Обучение закночилось")

    def clearSheet(self):
        self.blocks = [[0 for i in range(self.width)] for j in range(self.height)]
        self.drawPicture()

    def drawPicture(self):
        curXCoord = self.xStartCoord
        curYCoord = self.yStartCoord
        for line in self.blocks:
            for pixel in line:
                pg.draw.rect(self.scene,
                             (self.colorConstant - pixel, self.colorConstant - pixel, self.colorConstant - pixel),
                             (curXCoord, curYCoord, self.blockWidth, self.blockHeight))
                curXCoord += self.blockWidth
            curYCoord += self.blockHeight
            curXCoord = self.xStartCoord

    def updateSheet(self, xCoord, yCoord):
        curXIndex = xCoord // self.blockWidth
        curYIndex = yCoord // self.blockHeight
        for i in range(curXIndex - 1, curXIndex + 2):
            for j in range(curYIndex - 1, curYIndex + 2):

                if abs(curXIndex - i) + abs(curYIndex - j) == 2:
                    plusCoef = self.smallColorCoef
                elif abs(curXIndex - i) + abs(curYIndex - j) == 1:
                    plusCoef = self.bigColorCoef
                else:
                    plusCoef = self.colorConstant
                try:
                    if (self.blocks[abs(i)][abs(j)] + plusCoef) > 255:
                        self.blocks[abs(i)][abs(j)] = 255
                    else:
                        self.blocks[abs(i)][abs(j)] = plusCoef
                except IndexError:
                    pass
        self.drawPicture()

    def drawDigitLable(self, digit):
        pg.draw.rect(self.scene, (0, 0, 0),
                     (self.width * self.blockWidth + 150, self.height * self.blockHeight * 0.5, 100, 100))
        digitFont = pg.font.Font(None, 64)
        digitText = digitFont.render(digit, False, (180, 180, 180))
        self.scene.blit(digitText, (self.width * self.blockWidth + 150, self.height * self.blockHeight * 0.5))

    def drawLabel(self):
        labelFont = pg.font.Font(None, 32)
        labelText = labelFont.render("Очистить лист на 'C'.", False, (180, 180, 180))
        self.scene.blit(labelText, (self.width * self.blockWidth + 150, self.height * self.blockHeight * 0.1))
