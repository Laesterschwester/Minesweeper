import pygame

import bomb
import config
import random

class adjacentBombNumber:
    num = 0
    position = []
    def __init__(self, position, num):
        self.position = position
        self.num = num

    def drawNumber(self, display):
        color = config.LIGHT_BLUE
        if self.num == 1:
            color = config.LIGHT_BLUE
        if self.num == 2:
            color = config.GREEN
        if self.num == 3:
            color = config.RED
        if self.num == 4:
            color = config.VIOLET
        if self.num == 5:
            color = config.LIGHT_BLUE
        if self.num == 6:
            # color = config.
            pass
        if self.num == 7:
            # color = config.
            pass
        if self.num == 8:
            #color = config.
            pass
        #print(self.num)
        font = pygame.font.Font('freesansbold.ttf', 15)
        text = font.render(str(self.num), True, color)
        textRect = text.get_rect()
        textRect.center = (self.position[0]*(config.TILE_WIDTH+config.TILE_SPACING)+config.TILE_WIDTH // 2, (self.position[1]*(config.TILE_WIDTH+config.TILE_SPACING) )+ config.TILE_WIDTH// 2)
        display.blit(text, textRect)

class Grid:
    bombs = []
    adjacentBombs = []
    empty = []

    def __init__(self):
        numOfBombs = config.BOMB_COUNT
        if numOfBombs > config.NUMBER_OF_TILES_HEIGHT * config.NUMBER_OF_TILES_WIDTH:
            print("fuck youuuuuuuuuuuuuu!")
            numOfBombs = config.NUMBER_OF_TILES_WIDTH*config.NUMBER_OF_TILES_HEIGHT//2

        for x in range(config.NUMBER_OF_TILES_WIDTH):
            for y in range(config.NUMBER_OF_TILES_HEIGHT):
                self.empty.append([x, y])
        for i in range(numOfBombs):
            cond = True
            while cond:
                x = random.randint(0, config.NUMBER_OF_TILES_WIDTH-1)
                y = random.randint(0, config.NUMBER_OF_TILES_HEIGHT-1)
                position = [x, y]
                new_bomb = bomb.Bomb(position)

                if new_bomb not in self.bombs:
                    if position in self.empty:
                        self.bombs.append(new_bomb)
                        self.empty.remove(position)
                        cond = False
        for position in self.empty.copy():
            self.checkForAdjacentBombs(position)

    def getEmpty(self):
        return self.empty

    def checkForAdjacentBombs(self, position):
        num = 0
        for xShift in range(-1, 2):
            for yShift in range(-1, 2):
                if [xShift, yShift] == [0, 0]:
                    continue
                else:
                    x = position[0] + xShift
                    y = position[1] + yShift
                    for bombs in self.bombs:
                        if [x, y] == bombs.position:
                            num += 1
        if num != 0:
            self.empty.remove(position)
            new_num = adjacentBombNumber(position, num)
            self.adjacentBombs.append(new_num)

    def drawAdjBombNum(self, display):
        for adjBombs in self.adjacentBombs:
            adjBombs.drawNumber(display)

    def getBombs(self):
        return self.bombs

    def drawBombs(self, display):
        for bomb in self.bombs:
            bomb.drawBomb(display)
            """pygame.draw.circle(display, (0, 0, 0), (
            self.position[0] * (config.TILE_WIDTH + config.TILE_SPACING) + config.TILE_WIDTH // 2,
            self.position[1] * (config.TILE_WIDTH + config.TILE_SPACING) + config.TILE_WIDTH // 2), 7, 0)"""

    def drawGrid(self, display):
        maxIndex = (config.TILE_WIDTH+config.TILE_SPACING)
        self.drawBombs(display)
        self.drawAdjBombNum(display)

        for x in range(0, config.WINDOW_WIDTH, config.TILE_WIDTH + config.TILE_SPACING):
            pygame.draw.line(display, (40, 40, 40), (x-config.TILE_SPACING, 0), (x-config.TILE_SPACING, config.WINDOW_HEIGHT), config.TILE_SPACING)

        for y in range(0, config.WINDOW_HEIGHT, config.TILE_WIDTH + config.TILE_SPACING):
            pygame.draw.line(display, (40, 40, 40), (0, y-config.TILE_SPACING), (config.WINDOW_WIDTH, y-config.TILE_SPACING), config.TILE_SPACING)