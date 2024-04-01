import config
import pygame
import bombNumberDisplayGrid

class Tile:
    bomb = False
    flag = False
    revealed = False
    visible = True
    color = config.TILE_COLOR
    position = []
    width = config.TILE_WIDTH

    def __init__(self, position):
        self.position = position
        pass

    def isEmpty(self):
        if not self.bomb and not self.flag:
            return True
        else:
            return False

    def getBoolFlag(self):
        return self.visible

    def setFlag(self):
        self.flag = True

    def deleteFlag(self):
        self.flag = False

    def placeBomb(self):
        self.bomb = True

    def changeColor(self, col):
        self.color = col

    def clickTile(self, event):
        if event.button == 1 and not self.flag:
            self.reveal()
        elif event.button == 3:
            if self.flag == False and self.visible:
                self.flag = True
            else:
                self.flag = False

    def reveal(self):
        self.visible = False

    def drawTile(self, display):
        if self.visible:
            pygame.draw.rect(display, self.color, (self.position[0], self.position[1], self.width, self.width))