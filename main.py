import pygame as pg
import sys
from screen import Screen
from neuralNetwork import NeuralNetwork

screen = Screen()

screen.drawPicture()
neuraNetwork = NeuralNetwork()

neuraNetwork.learning()

pg.display.update()
curPos = [-1, -1]

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_c:
                screen.clearSheet()
                pg.display.update()

    pressed = pg.mouse.get_pressed()
    pos = pg.mouse.get_pos()
    xDiv = abs(curPos[1] - pos[1]) >= screen.blockWidth
    yDiv = abs(curPos[0] - pos[0]) >= screen.blockHeight
    if pressed[0] and (xDiv or yDiv):
        curPos = pos
        screen.updateSheet(pos[1], pos[0])
        screen.drawDigitLable(digit=neuraNetwork.predict(screen.blocks))
        pg.display.update()
